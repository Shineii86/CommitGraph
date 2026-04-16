<div align="center">

[![Commit Graph Generator Banner](https://raw.githubusercontent.com/Shineii86/CommitGraph/main/images/CommitGraph.png)](https://github.com/Shineii86/CommitGraph)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shineii86/CommitGraph/blob/main/notebooks/CommitGraph.ipynb)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![GitHub Stars](https://img.shields.io/github/stars/Shineii86/CommitGraph?style=for-the-badge)](https://github.com/Shineii86/CommitGraph/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Shineii86/CommitGraph?style=for-the-badge)](https://github.com/Shineii86/CommitGraph/fork)

A **fully automated** Python script that runs in **Google Colab** to generate backdated commits and customize your GitHub contribution graph.

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
  - [Random Commit Pattern](#-random-commit-pattern)
  - [🎨 Custom Text Mode](#-custom-text-mode)
- [How It Works](#-how-it-works-technical-overview)
- [Troubleshooting](#-troubleshooting)
- [Credits & Acknowledgments](#-credits--acknowledgments)
- [License & Disclaimer](#-license--disclaimer)

---

## 🎯 What is This Tool?

This tool generates backdated commits over a specified date range, allowing you to customize the appearance of your GitHub contribution graph.

**Two Modes Available:**

1. **Random Commit Pattern** – Creates a gradually increasing density of commits (ramp‑up effect) over a date range.
2. **🎨 Custom Text Mode** – Draws words like `HELLO` or `GITHUB` directly onto your contribution graph using a 5×7 pixel font. Each letter is mapped to specific days, creating a clean, pixel‑art style message.

**Common Use Cases:**
- Experimenting with Git's backdating capabilities for educational purposes.
- Creating a specific visual pattern or message on your contribution graph for fun.
- Understanding how GitHub's contribution tracking works.

> ⚠️ **Note:** This tool does **not** unlock any GitHub achievement. It is purely a customization utility.

---

## ✅ Why Use This Method?

| Feature                      | Benefit                                                                 |
|------------------------------|-------------------------------------------------------------------------|
| ☁️ **No PC Required**         | Runs entirely in Google Colab (cloud‑based). Works on any device with a browser. |
| 📅 **Flexible Date Range**    | Specify any start and end date for your commit pattern.                  |
| 📈 **Customizable Density**   | Control the minimum and maximum commits per day.                         |
| 🎨 **Draw Text**              | Spell words using the contribution graph's green squares.                |
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

Inside the Colab notebook, you'll find a single configuration cell with form fields. Choose between the **Random Pattern** (default) and **Custom Text Mode** by toggling `USE_CUSTOM_TEXT`.

### 3️⃣ Run the Notebook

Click **Runtime → Run all** (or press `Ctrl+F9`). The notebook will:
- Install `GitPython`
- Clone your repository
- Generate backdated commits according to your chosen mode
- Force-push the new history to GitHub

You'll see real‑time output like:

```
📅 Commit Graph Generator for user 'Shineii86'
Repository: commit-graph-demo

🎨 Drawing text: "HELLO"
   Starting 0 week(s) after 2026-04-01
   3 commit(s) per pixel

📌 2026-04-01: 9 commits
📌 2026-04-02: 6 commits
...
✅ Created commits on 21 days to spell "HELLO".

⏫ Pushing to remote...
✅ Force push complete.

✨ Done! Your contribution graph will update shortly.
📊 Visit: https://github.com/Shineii86
```

### 4️⃣ View Your Contribution Graph

1. Go to your GitHub profile: `https://github.com/YOUR_USERNAME`
2. The contribution graph will update within a few minutes to reflect the new commits.

---

## ⚙️ Configuration Options

All parameters are adjustable directly in the Colab form. The form is divided into three sections: **Common Settings**, **Custom Text Mode**, and **Random Pattern Mode**.

### Common Settings (Always Required)

| Variable              | Description                                      | Example Value               |
|-----------------------|--------------------------------------------------|-----------------------------|
| `GITHUB_USERNAME`     | Your GitHub handle                               | `"Shineii86"`               |
| `GITHUB_TOKEN`        | Personal Access Token (keep secret!)             | `"ghp_abc123..."`           |
| `REPO_NAME`           | Target repository (must exist under your account)| `"commit-graph-demo"`       |
| `FORCE_PUSH`          | Overwrite remote history (required)              | `True`                      |
| `USE_CUSTOM_TEXT`     | Toggle between **Custom Text** (`True`) and **Random Pattern** (`False`). | `False` |

---

### 📈 Random Commit Pattern

Used when `USE_CUSTOM_TEXT = False`. Creates commits with a linear ramp‑up in density.

| Parameter            | Default       | Description                                                                 |
|----------------------|---------------|-----------------------------------------------------------------------------|
| `START_DATE`         | `"2026-04-01"`| First date to create commits.                                                |
| `END_DATE`           | `"2026-04-15"`| Last date to create commits.                                                 |
| `MIN_COMMITS_START`  | `0`           | Minimum commits on the first day.                                            |
| `MAX_COMMITS_START`  | `5`           | Maximum commits on the first day.                                            |
| `MIN_COMMITS_END`    | `5`           | Minimum commits on the last day.                                             |
| `MAX_COMMITS_END`    | `10`          | Maximum commits on the last day.                                             |

**Commit Density Logic**  
The script linearly interpolates the commit count ranges from start to end. For a constant density, set the start and end min/max values equal.

---

### 🎨 Custom Text Mode

Used when `USE_CUSTOM_TEXT = True`. Draws a word or phrase using the contribution graph as a canvas.

| Parameter                  | Default       | Description                                                                                                   |
|----------------------------|---------------|---------------------------------------------------------------------------------------------------------------|
| `CUSTOM_TEXT`              | `"HELLO"`     | The word to draw. Supported characters: uppercase `A-Z`, digits `0-9`, space, `.`, `!`, `?`.                  |
| `START_DATE`               | `"2026-04-01"`| The Sunday of the week where drawing begins (the script auto‑adjusts to Sunday if a different day is given).  |
| `TEXT_START_OFFSET_WEEKS`  | `0`           | Number of empty weeks to skip after `START_DATE` before drawing the text (shifts the text to the right).      |
| `COMMITS_PER_PIXEL`        | `3`           | How many commits to create for each "on" pixel. Higher numbers = darker green squares (max shade usually at 4–5 commits). |

#### How Custom Text Works

- Each character is rendered using a **5×7 pixel font**. The top row corresponds to **Sunday**, the bottom row to **Saturday**.
- Characters are placed side‑by‑side with a 1‑column gap.
- The script calculates the exact days that need commits and pushes them with backdated timestamps.

**Example: Drawing "HI"**

| Setting                | Value                 |
|------------------------|-----------------------|
| `CUSTOM_TEXT`          | `"HI"`                |
| `START_DATE`           | `"2026-04-05"` (a Sunday) |
| `COMMITS_PER_PIXEL`    | `3`                   |

The result on your graph:

```
Sun Mon Tue Wed Thu Fri Sat
  █  █              █  █     ← 'H' (first week)
  █  █              █  █
  █  █              █  █
  ████              ████
  █  █              █  █
  █  █              █  █
  █  █              █  █

Sun Mon Tue Wed Thu Fri Sat
  ████                ██     ← 'I' (second week)
   ██                 ██
   ██                 ██
   ██                 ██
   ██                 ██
   ██                 ██
  ████                ██
```

> 💡 **Tip:** Because GitHub contribution weeks start on Sunday, choose a `START_DATE` that is a Sunday for predictable alignment.

---

## 🔬 How It Works (Technical Overview)

The script performs the following steps:

1. **Clones the Repository**: Uses your Personal Access Token to clone the specified repository into the Colab environment.
2. **Configures Git User**: Sets the commit author and email to your GitHub identity.
3. **Generates Commits**:
   - **Random Mode**: Iterates through each day, calculates a random number of commits, and creates them with backdated timestamps.
   - **Custom Text Mode**: Converts the input string to pixel coordinates, groups them by day, and creates the required number of commits per day.
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
| Commits appear on wrong dates                     | Verify the date format is `YYYY-MM-DD`. For Custom Text mode, ensure `START_DATE` is a Sunday or let the script auto‑adjust. |
| Custom text characters are missing or misaligned  | Only uppercase letters, digits, and the symbols `. ! ?` are supported. The script will skip unsupported characters. |

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
