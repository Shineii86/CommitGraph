# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] - 2026-05-22

### Fixed
- **Critical: `NameError` in DRY_RUN + Custom Text mode** — `max_week` was referenced in `preview_graph()` call before it was defined. Moved pixel computation and `max_week` calculation above the dry-run check.
- **Lowercase letter bitmaps** — Previous lowercase letters were identical copies of uppercase. Replaced all 26 lowercase characters (a-z) with distinct, properly-sized pixel designs (e.g., `a` now has a flat top, `b` has an ascender, etc.).
- **`'END_DATE' in locals()` always True** — Removed this dead check since `END_DATE` is always defined in the config section. The custom text mode now uses `max_week` to determine date range instead.

### Added
- **Modular project structure** — Split monolithic notebook into reusable Python modules:
  - `src/font.py` — 5×7 pixel font bitmaps with `text_to_pixels()` and `get_supported_chars()`
  - `src/config.py` — Configuration dataclasses (`AppConfig`, `GitHubConfig`, etc.) with validation
  - `src/utils.py` — Utility functions (progress bar, commit estimation, ASCII graph preview)
  - `src/generator.py` — Core commit generation engine (clone, commit, push logic)
  - `src/__init__.py` — Package metadata
- **Standalone CLI** (`commitgraph.py`) — Run directly from the command line without Google Colab. Supports all features via `argparse` flags.
- **`requirements.txt`** — Explicit dependency declaration for pip installs.
- **Additional symbols in font** — Added `_ ~ ^ < > [ ] { } | \ $ % `` ` `` to the pixel font (total: 95 characters).
- **Configuration validation** — `AppConfig.validate()` checks for missing tokens, empty text, invalid dates, and other errors before execution.

### Changed
- **Notebook refactored** — Colab notebook is now a thin wrapper that imports from `src/` modules instead of containing all logic inline. Easier to maintain and test.
- **README updated** — Added project structure diagram, standalone CLI usage section, and CLI options table.

## [1.2.0] - 2026-05-21

### Added
- **Lowercase letter support** (a-z) — auto-mapped to pixel font bitmaps.
- **22 new symbols** — `@ # & + - = : ; , ( ) / ' " *` and more. Total: 80 characters.
- **Dry-run preview mode** (`DRY_RUN`) — see the contribution pattern before committing. Shows ASCII graph for custom text, day-by-day breakdown for random mode.
- **Intermediate push** (`INTERMEDIATE_PUSH_DAYS`) — push every N days during long runs to avoid losing progress on failure.
- **Commit count estimation** — shows total commits before generation starts.
- **Visual progress bar** — `[████████░░░░] 67%` style output during random pattern generation.
- **ASCII graph preview** — renders the custom text pattern as a grid before committing.

### Changed
- Updated README with new configuration options and feature descriptions.

## [1.1.1] - 2026-05-21

### Changed
- `GITHUB_EMAIL` now defaults to empty and **auto-detects** the correct noreply email from the GitHub token via the API.
- Removed hardcoded email — works for any user out of the box.
- Added auto-detection error handling with clear fallback instructions.
- Updated README troubleshooting table with contribution graph fix guidance.

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
