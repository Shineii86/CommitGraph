<div align="center">

[![Commit Graph Generator Banner](https://raw.githubusercontent.com/Shineii86/CommitGraph/main/images/CommitGraph.png)](https://github.com/Shineii86/CommitGraph)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shineii86/CommitGraph/blob/main/notebooks/CommitGraph.ipynb)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![GitHub Stars](https://img.shields.io/github/stars/Shineii86/CommitGraph?style=for-the-badge)](https://github.com/Shineii86/CommitGraph/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Shineii86/CommitGraph?style=for-the-badge)](https://github.com/Shineii86/CommitGraph/fork)

A **fully automated** Python script that runs in **Google Colab** to generate backdated commits and customize your GitHub contribution graph — all from your browser.

</div>

---

> [!WARNING]
> **This script creates backdated commits to artificially populate your GitHub contribution graph.**
> - **Use responsibly.** Artificially inflating contributions may be viewed negatively by potential employers or collaborators who review your profile.
> - You need a **GitHub Personal Access Token (classic)** with `repo` scope to push commits.
> - The script **force-pushes** to your repository, overwriting its commit history. **Use a dedicated, empty repository** to avoid losing important work.
> - This tool is intended for **educational purposes and personal experimentation** only.

---

## 📖 Table of Contents

- [What is This Tool?](#-what-is-this-tool)
- [Why Use This Method?](#-why-use-this-method)
- [Prerequisites](#-prerequisites)
- [Step-by-Step Guide](#-step-by-step-guide)
- [Configuration Options](#-configuration-options)
- [How It Works](#-how-it-works-technical-overview)
- [Troubleshooting](#-troubleshooting)
- [Credits & Acknowledgments](#-credits--acknowledgments)
- [License & Disclaimer](#-license--disclaimer)

---

## 🎯 What is This Tool?

This tool generates backdated commits over a specified date range, allowing you to customize the appearance of your GitHub contribution graph. It creates a commit pattern that starts sparse and becomes increasingly dense toward the end date, simulating a period of intense development activity.

**Common Use Cases:**
- Experimenting with Git's backdating capabilities for educational purposes.
- Creating a specific visual pattern on your contribution graph for fun.
- Understanding how GitHub's contribution tracking works.

> ⚠️ **Note:** This tool does **not** unlock any GitHub achievement. It is purely a customization utility.

---

## ✅ Why Use This Method?

| Feature                      | Benefit                                                                 |
|------------------------------|-------------------------------------------------------------------------|
| ☁️ **No PC Required**         | Runs entirely in Google Colab (cloud‑based). Works on any device with a browser. |
| 📅 **Flexible Date Range**    | Specify any start and end date for your commit pattern.                  |
| 📈 **Customizable Density**   | Control the minimum and maximum commits per day at both ends of the range. |
| 🔁 **Fully Automated**        | Clones, commits, and force-pushes automatically.                         |
| 📦 **Minimal Dependencies**   | Only uses `GitPython` and standard libraries.                            |

---

## 🧰 Prerequisites

Before you begin, make sure you have:

1. **A GitHub account**.
2. **An empty or dedicated repository** where you have **write access** (create a new one to avoid losing real work).
3. **A GitHub Personal Access Token (Classic)** with `repo` scope.

### 🔐 How to Get a Personal Access Token

1. Go to **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**.
2. Click **Generate new token (classic)**.
3. Give it a name (e.g., `Commit Graph Generator`).
4. Under **Select scopes**, check **`repo`** (this grants full control of your repositories).
5. Click **Generate token** and **copy the token immediately** — you won't see it again.

> 🔒 **Keep this token secret.** Never share it with anyone or upload it to a public place.

---

## 📥 How to Deploy

### 1️⃣ One‑Click Colab

<a href="https://colab.research.google.com/github/Shineii86/CommitGraph/blob/main/notebooks/CommitGraph.ipynb">
  <img src="https://user-images.githubusercontent.com/125879861/255389999-a0d261cf-893a-46a7-9a3d-2bb52811b997.png" alt="Open In Colab" width="200px">
</a>

### 2️⃣ Fill in the Configuration Form

Inside the Colab notebook, you'll find a single configuration cell with form fields:

| Variable              | Description                                      | Example Value               |
|-----------------------|--------------------------------------------------|-----------------------------|
| `GITHUB_USERNAME`     | Your GitHub handle                               | `"Shineii86"`               |
| `GITHUB_TOKEN`        | Personal Access Token (keep secret!)             | `"ghp_abc123..."`           |
| `REPO_NAME`           | Target repository (must exist under your account)| `"commit-graph-demo"`       |
| `START_DATE`          | First date for commits (YYYY-MM-DD)              | `"2026-04-01"`              |
| `END_DATE`            | Last date for commits (YYYY-MM-DD)               | `"2026-04-15"`              |
| `MIN_COMMITS_START`   | Minimum commits/day at beginning of range        | `0`                         |
| `MAX_COMMITS_START`   | Maximum commits/day at beginning of range        | `2`                         |
| `MIN_COMMITS_END`     | Minimum commits/day at end of range              | `20`                        |
| `MAX_COMMITS_END`     | Maximum commits/day at end of range              | `29`                        |
| `FORCE_PUSH`          | Overwrite remote history (required)              | `True`                      |

### 3️⃣ Run the Notebook

Click **Runtime → Run all** (or press `Ctrl+F9`). The notebook will:
- Install `GitPython`
- Clone your repository
- Generate backdated commits over the specified date range
- Force-push the new history to GitHub

You'll see real‑time output like:

```
📅 Commit Graph Generator for user 'Shineii86'
Repository: commit-graph-demo
Date range: 2026-04-01 → 2026-04-15

Total days: 15
📥 Cloning repository...

🚀 Starting commit generation...

📌 2026-04-01: 1 commits
📌 2026-04-02: 2 commits
...
📌 2026-04-14: 24 commits
📌 2026-04-15: 28 commits

🎉 All commits created. Now pushing to remote...
✅ Force push complete.

✨ Done! Your contribution graph should reflect the new commits shortly.
📊 Visit: https://github.com/Shineii86
```

### 4️⃣ View Your Contribution Graph

1. Go to your GitHub profile: `https://github.com/YOUR_USERNAME`
2. The contribution graph will update within a few minutes to reflect the new commits.

---

## ⚙️ Configuration Options

All parameters are adjustable directly in the Colab form:

| Parameter            | Default | Description                                                                 |
|----------------------|---------|-----------------------------------------------------------------------------|
| `START_DATE`         | `"2026-04-01"` | First date to create commits. |
| `END_DATE`           | `"2026-04-15"` | Last date to create commits. |
| `MIN_COMMITS_START`  | `0`      | Minimum commits on the first day. |
| `MAX_COMMITS_START`  | `2`      | Maximum commits on the first day. |
| `MIN_COMMITS_END`    | `20`     | Minimum commits on the last day. |
| `MAX_COMMITS_END`    | `29`     | Maximum commits on the last day. |
| `FORCE_PUSH`         | `True`   | Must be `True` to overwrite remote history with backdated commits. |

### Commit Density Logic

The script linearly interpolates the commit count ranges from the start date to the end date. For example:
- Day 1: 0–2 commits
- Day 8 (midpoint): 10–15 commits
- Day 15: 20–29 commits

This creates a gradual "ramp-up" effect on your contribution graph.

### Customizing the Pattern

- For a **constant density**, set `MIN_COMMITS_START = MIN_COMMITS_END` and `MAX_COMMITS_START = MAX_COMMITS_END`.
- For a **decreasing pattern**, swap the start and end values.
- For a **single spike**, set a short date range with high commit counts.

---

## 🔬 How It Works (Technical Overview)

The script performs the following steps:

1. **Clones the Repository**: Uses your Personal Access Token to clone the specified repository into the Colab environment.
2. **Configures Git User**: Sets the commit author and email to your GitHub identity.
3. **Iterates Through Dates**: For each day in the date range:
   - Calculates a random number of commits between the interpolated min/max values.
   - For each commit:
     - Writes a timestamp to `data.json`.
     - Stages the file.
     - Creates a commit with the author and committer dates explicitly set to the target date using Git's `--date` equivalent via `GitPython`.
4. **Force Pushes**: Overwrites the remote repository's history with the new commit chain. This is necessary because backdating changes the commit timestamps, altering the existing history.

> ⚠️ **Force push is destructive.** It replaces the entire commit history on the remote branch. Always use a dedicated repository.

---

## 🆘 Troubleshooting

| Issue                                             | Solution                                                                                     |
|---------------------------------------------------|----------------------------------------------------------------------------------------------|
| `github.GithubException.BadCredentialsException`  | Your Personal Access Token is incorrect or expired. Generate a new one.                       |
| `Permission denied` or `Authentication failed`    | Ensure your token has the `repo` scope checked.                                               |
| Repository not found                              | Verify the repository name is correct and exists under your account.                          |
| Contribution graph not updating                   | Wait a few minutes—GitHub's graph updates are not instant. Also ensure the repository is **public** or that you've enabled **private contributions** in your profile settings. |
| `GitCommandError: cannot push`                    | Make sure `FORCE_PUSH` is set to `True`. Backdated commits require force-pushing.             |
| Commits appear on wrong dates                     | Verify the date format is `YYYY-MM-DD` and that your system timezone doesn't affect the commit timestamps (the script uses UTC internally). |

---

## 📄 License & Disclaimer

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

> [!WARNING]
> This script is intended for **educational purposes and personal experimentation** only. Artificially inflating your contribution graph may be viewed negatively by potential employers or collaborators. The author is not responsible for any consequences arising from misuse of this tool, including but not limited to damage to professional reputation or violation of platform terms.

---

### 🔗 Quick Links

- [Google Colab](https://colab.research.google.com/)
- [GitHub Personal Access Tokens](https://github.com/settings/tokens)
- [GitPython Documentation](https://gitpython.readthedocs.io/)

---

## 💕 Loved My Work?

🚨 [Follow me on GitHub](https://github.com/Shineii86)

⭐ [Give a star to this project](https://github.com/Shineii86/CommitGraph)

<div align="center">

<a href="https://github.com/Shineii86/CommitGraph">
<img src="https://github.com/Shineii86/AniPay/blob/main/Source/Banner6.png" alt="Banner">
</a>
  
  *For inquiries or collaborations*
     
[![Telegram Badge](https://img.shields.io/badge/-Telegram-2CA5E0?style=flat&logo=Telegram&logoColor=white)](https://telegram.me/Shineii86 "Contact on Telegram")
[![Instagram Badge](https://img.shields.io/badge/-Instagram-C13584?style=flat&logo=Instagram&logoColor=white)](https://instagram.com/ikx7.a "Follow on Instagram")
[![Pinterest Badge](https://img.shields.io/badge/-Pinterest-E60023?style=flat&logo=Pinterest&logoColor=white)](https://pinterest.com/ikx7a "Follow on Pinterest")
[![Gmail Badge](https://img.shields.io/badge/-Gmail-D14836?style=flat&logo=Gmail&logoColor=white)](mailto:ikx7a@hotmail.com "Send an Email")

  <sup><b>Copyright © 2026 <a href="https://telegram.me/Shineii86">Shinei Nouzen</a> All Rights Reserved</b></sup>

![Last Commit](https://img.shields.io/github/last-commit/Shineii86/CommitGraph?style=for-the-badge)

</div>
