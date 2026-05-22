#!/usr/bin/env python3
"""
CommitGraph — GitHub Contribution Graph Generator

Standalone CLI entry point. Can be run outside of Google Colab.

Usage:
    python commitgraph.py --token ghp_xxx --repo my-repo --text HELLO
    python commitgraph.py --token ghp_xxx --repo my-repo --start 2026-04-01 --end 2026-04-15
    python commitgraph.py --token ghp_xxx --repo my-repo --text HELLO --dry-run

Requires: pip install gitpython
"""

import argparse
import sys

from src.config import AppConfig, GitHubConfig, CustomTextConfig, RandomPatternConfig, GeneralConfig
from src.generator import run


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate backdated commits to customize your GitHub contribution graph.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Custom text:  python commitgraph.py --token ghp_xxx --repo demo --text HELLO
  Random:       python commitgraph.py --token ghp_xxx --repo demo --start 2026-04-01 --end 2026-04-15
  Dry run:      python commitgraph.py --token ghp_xxx --repo demo --text HI --dry-run
        """,
    )

    # Required
    parser.add_argument("--token", required=True, help="GitHub Personal Access Token")
    parser.add_argument("--repo", required=True, help="Target repository name")

    # Optional auth
    parser.add_argument("--username", default="Shineii86", help="GitHub username")
    parser.add_argument("--email", default="", help="GitHub noreply email (auto-detected if omitted)")

    # Mode selection
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--text", help="Text to draw on contribution graph (enables custom text mode)")
    mode.add_argument("--random", action="store_true", help="Use random pattern mode (default)")

    # Custom text options
    parser.add_argument("--offset-weeks", type=int, default=0, help="Weeks to skip before drawing text")
    parser.add_argument("--commits-per-pixel", type=int, default=3, help="Commits per pixel (darker = more)")

    # Random pattern options
    parser.add_argument("--start", default="2026-04-01", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", default="2026-04-15", help="End date (YYYY-MM-DD)")
    parser.add_argument("--min-start", type=int, default=0, help="Min commits/day at start")
    parser.add_argument("--max-start", type=int, default=5, help="Max commits/day at start")
    parser.add_argument("--min-end", type=int, default=5, help="Min commits/day at end")
    parser.add_argument("--max-end", type=int, default=10, help="Max commits/day at end")

    # General
    parser.add_argument("--no-force-push", action="store_true", help="Don't force push")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, don't create commits")
    parser.add_argument("--push-every", type=int, default=0, help="Intermediate push every N days")

    return parser.parse_args()


def main():
    args = parse_args()

    config = AppConfig(
        github=GitHubConfig(
            username=args.username,
            token=args.token,
            email=args.email,
            repo_name=args.repo,
            force_push=not args.no_force_push,
        ),
        custom_text=CustomTextConfig(
            enabled=bool(args.text),
            text=args.text or "HELLO",
            start_offset_weeks=args.offset_weeks,
            commits_per_pixel=args.commits_per_pixel,
        ),
        random_pattern=RandomPatternConfig(
            start_date=args.start,
            end_date=args.end,
            min_commits_start=args.min_start,
            max_commits_start=args.max_start,
            min_commits_end=args.min_end,
            max_commits_end=args.max_end,
        ),
        general=GeneralConfig(
            dry_run=args.dry_run,
            intermediate_push_days=args.push_every,
        ),
        start_date=args.start,
    )

    run(config)


if __name__ == "__main__":
    main()
