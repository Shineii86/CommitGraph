# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2026-05-21

### Fixed
- **Critical: Email format mismatch** — Changed from `username@users.noreply.github.com` to `ID+username@users.noreply.github.com` (e.g., `157171073+Shineii86@users.noreply.github.com`). This was the root cause of commits not counting toward the GitHub contribution graph.
- **Author/Committer email consistency** — All commit creation paths now use the correct `GITHUB_EMAIL` field instead of generating it from the username.

### Added
- **`GITHUB_EMAIL` configuration field** in the Colab form so users can set their correct noreply email.
- **`.gitignore` file** — excludes `data.json`, `__pycache__/`, `.DS_Store`, and other junk files from version control.
- **Auto-generated `.gitignore`** — the notebook now creates a `.gitignore` in the target repository automatically.

### Improved
- Cleaner commit history by excluding `data.json` from tracked files.

## [1.0.0] - 2026-04-16

### Added
- Initial release of Commit Graph Generator.
- Random commit pattern mode with configurable date range and density.
- Custom text mode (5×7 pixel font) for drawing words on the contribution graph.
- Google Colab notebook with form-based configuration.
- Full README with troubleshooting guide and documentation.
- MIT License.
