"""
Commit generation engine for CommitGraph.

Handles cloning repos, creating backdated commits, and pushing.
Supports both custom text and random pattern modes.
"""

import json
import os
import random
import time
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta

from git import Actor, Repo

from .config import AppConfig
from .font import text_to_pixels
from .utils import estimate_commits, parse_date, preview_graph, progress_bar


GITIGNORE_CONTENT = """\
# Data files
data.json

# Python
__pycache__/
*.pyc
*.pyo

# OS
.DS_Store
Thumbs.db
"""


def detect_email(token: str) -> str:
    """
    Auto-detect the GitHub noreply email from a Personal Access Token.

    Returns the email string, or raises RuntimeError on failure.
    """
    print("🔍 Auto-detecting GitHub noreply email from token...")
    try:
        req = urllib.request.Request(
            "https://api.github.com/user",
            headers={
                "Authorization": f"token {token}",
                "Accept": "application/vnd.github.v3+json",
                "User-Agent": "CommitGraphGenerator",
            },
        )
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            gh_id = data["id"]
            gh_login = data["login"]
            email = f"{gh_id}+{gh_login}@users.noreply.github.com"
            print(f"✅ Detected: {email}")
            return email
    except Exception as e:
        raise RuntimeError(
            f"Could not auto-detect email: {e}\n"
            "Please set GITHUB_EMAIL manually.\n"
            "Find it at: https://github.com/settings/emails"
        )


def setup_repo(config: AppConfig) -> tuple[Repo, str, str]:
    """
    Clone or open the target repository, configure git user, and set up .gitignore.

    Returns:
        (repo, origin_url, data_file_path)
    """
    gh = config.github
    repo_url = f"https://{gh.username}:{gh.token}@github.com/{gh.username}/{gh.repo_name}.git"
    local_dir = f"/content/{gh.repo_name}"
    data_file = "data.json"

    if os.path.exists(local_dir):
        try:
            repo = Repo(local_dir)
            print("📂 Opening existing repository...")
            origin = repo.remote(name="origin")
            origin.pull()
        except Exception:
            print("⚠️  Existing directory is not a valid repo. Re-cloning...")
            import shutil
            shutil.rmtree(local_dir)
            repo = Repo.clone_from(repo_url, local_dir)
    else:
        print("📥 Cloning repository...")
        repo = Repo.clone_from(repo_url, local_dir)

    # Configure git identity
    writer = repo.config_writer()
    writer.set_value("user", "name", gh.username).release()
    writer.set_value("user", "email", gh.email).release()

    # Write .gitignore
    gitignore_path = os.path.join(local_dir, ".gitignore")
    with open(gitignore_path, "w") as f:
        f.write(GITIGNORE_CONTENT)
    repo.index.add([".gitignore"])

    data_path = os.path.join(local_dir, data_file)
    return repo, repo_url, data_path


def _push(repo: Repo, force: bool = True) -> None:
    """Push to remote, optionally with force."""
    origin = repo.remote(name="origin")
    if force:
        origin.push(force=True)
    else:
        origin.push()


def generate_custom_text(config: AppConfig, repo: Repo, data_path: str) -> None:
    """Generate commits that spell text on the contribution graph."""
    ct = config.custom_text
    gh = config.github
    data_file = "data.json"

    print(f'\n🎨 Drawing text: "{ct.text}"')
    print(f"   Starting {ct.start_offset_weeks} week(s) after {config.start_date}")
    print(f"   {ct.commits_per_pixel} commit(s) per pixel\n")

    # Parse start date and align to Sunday
    start_date = parse_date(config.start_date)
    days_to_sunday = (start_date.weekday() + 1) % 7
    base_sunday = start_date - timedelta(days=days_to_sunday)

    # Get pixel coordinates
    pixels = text_to_pixels(ct.text, ct.start_offset_weeks)
    if not pixels:
        print("⚠️  No pixels to draw. Check your text and supported characters.")
        return

    max_week = max(w for w, d in pixels)

    # Estimate
    est_total, est_days = estimate_commits(pixels, ct.commits_per_pixel)
    print(f"📊 Estimated: {est_total} commits across {est_days} days")

    # DRY RUN — now safe because max_week is computed above
    if config.general.dry_run:
        preview_graph(pixels, max_week)
        print("🔍 DRY RUN — no commits created.")
        return

    # Group by (week, day)
    day_commit_counts: dict[tuple[int, int], int] = defaultdict(int)
    for week, day in pixels:
        day_commit_counts[(week, day)] += ct.commits_per_pixel

    # Generate commits
    author = Actor(gh.username, gh.email)
    day_count = 0

    for week in range(max_week + 1):
        for day in range(7):
            current = base_sunday + timedelta(weeks=week, days=day)
            num_commits = day_commit_counts.get((week, day), 0)

            for i in range(num_commits):
                payload = {
                    "date": current.isoformat(),
                    "custom_text": ct.text,
                    "pixel_commit": i + 1,
                }
                with open(data_path, "w") as f:
                    json.dump(payload, f, indent=2)

                repo.index.add([data_file])
                msg = f"🎨 {ct.text} – {current.strftime('%Y-%m-%d')} ({i + 1}/{num_commits})"
                repo.index.commit(
                    msg,
                    author=author,
                    committer=author,
                    author_date=current.strftime("%Y-%m-%dT%H:%M:%S"),
                    commit_date=current.strftime("%Y-%m-%dT%H:%M:%S"),
                )
                time.sleep(0.05)

            if num_commits > 0:
                print(f"📌 {current.strftime('%Y-%m-%d')}: {num_commits} commits")
                day_count += 1

            # Intermediate push
            ipd = config.general.intermediate_push_days
            if ipd > 0 and day_count > 0 and day_count % ipd == 0:
                print(f"\n⏫ Intermediate push after {day_count} days of commits...")
                _push(repo, gh.force_push)
                print("✅ Intermediate push done.")

    print(f'\n✅ Created commits on {day_count} days to spell "{ct.text}".')


def generate_random_pattern(config: AppConfig, repo: Repo, data_path: str) -> None:
    """Generate commits with a random density ramp-up pattern."""
    rp = config.random_pattern
    gh = config.github
    data_file = "data.json"

    start_date = parse_date(rp.start_date)
    end_date = parse_date(rp.end_date)
    total_days = (end_date - start_date).days + 1

    if total_days <= 0:
        print("❌ END_DATE must be after START_DATE.")
        return

    est_avg = (
        rp.min_commits_start + rp.max_commits_start
        + rp.min_commits_end + rp.max_commits_end
    ) / 4
    est_total = int(est_avg * total_days)
    print(f"📊 Estimated: ~{est_total} commits across {total_days} days")

    # DRY RUN
    if config.general.dry_run:
        print("\n📅 Day-by-day preview:")
        for day_offset in range(total_days):
            cd = start_date + timedelta(days=day_offset)
            progress = day_offset / max(total_days - 1, 1)
            mn = int(rp.min_commits_start + (rp.min_commits_end - rp.min_commits_start) * progress)
            mx = int(rp.max_commits_start + (rp.max_commits_end - rp.max_commits_start) * progress)
            print(f"  {cd.strftime('%Y-%m-%d')}: {mn}-{mx} commits")
        print("\n🔍 DRY RUN — no commits created.")
        return

    print(f"\n📊 Random pattern from {rp.start_date} to {rp.end_date}")

    author = Actor(gh.username, gh.email)

    for day_offset in range(total_days):
        current_date = start_date + timedelta(days=day_offset)
        progress = day_offset / max(total_days - 1, 1)

        min_c = int(rp.min_commits_start + (rp.min_commits_end - rp.min_commits_start) * progress)
        max_c = int(rp.max_commits_start + (rp.max_commits_end - rp.max_commits_start) * progress)
        commits_today = random.randint(min_c, max_c)

        for commit_num in range(commits_today):
            payload = {
                "date": current_date.isoformat(),
                "commit_number": commit_num + 1,
                "total_today": commits_today,
            }
            with open(data_path, "w") as f:
                json.dump(payload, f, indent=2)

            repo.index.add([data_file])
            msg = f"📅 Commit for {current_date.strftime('%Y-%m-%d')} ({commit_num + 1}/{commits_today})"
            repo.index.commit(
                msg,
                author=author,
                committer=author,
                author_date=current_date.strftime("%Y-%m-%dT%H:%M:%S"),
                commit_date=current_date.strftime("%Y-%m-%dT%H:%M:%S"),
            )
            time.sleep(0.05)

        if commits_today > 0:
            print(f"📌 {current_date.strftime('%Y-%m-%d')}: {commits_today} commits")

        # Intermediate push
        ipd = config.general.intermediate_push_days
        if ipd > 0 and (day_offset + 1) % ipd == 0:
            print(f"\n⏫ Intermediate push after {day_offset + 1} days...")
            _push(repo, gh.force_push)
            print("✅ Intermediate push done.")

        if (day_offset + 1) % 30 == 0:
            print(f"⏳ Progress: {progress_bar(day_offset + 1, total_days)}")

    print("\n🎉 All random commits created.")


def run(config: AppConfig) -> None:
    """
    Main entry point: validate config, set up repo, generate commits, push.

    This is what the notebook calls.
    """
    # Validate
    errors = config.validate()
    if errors:
        print("❌ Configuration errors:")
        for err in errors:
            print(f"   • {err}")
        return

    # Resolve email
    if not config.github.email.strip():
        config.github.email = detect_email(config.github.token)
    else:
        print(f"📧 Using provided email: {config.github.email}")

    # Setup repo
    repo, _, data_path = setup_repo(config)

    print(f"\n📅 Commit Graph Generator for user '{config.github.username}'")
    print(f"Repository: {config.github.repo_name}\n")

    # Generate
    if config.custom_text.enabled:
        generate_custom_text(config, repo, data_path)
    else:
        generate_random_pattern(config, repo, data_path)

    # Final push
    print("\n⏫ Pushing to remote...")
    _push(repo, config.github.force_push)
    print("✅ Force push complete." if config.github.force_push else "✅ Push complete.")

    print(f"\n✨ Done! Your contribution graph will update shortly.")
    print(f"📊 Visit: https://github.com/{config.github.username}")
    print("\n---")
    print("📅 Generator By [Shinei Nouzen](https://github.com/Shineii86/CommitGraph)")
