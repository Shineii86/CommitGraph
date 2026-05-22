"""
Configuration dataclasses for CommitGraph.

Separates configuration from logic, making it easy to validate,
extend, and test.
"""

from dataclasses import dataclass, field


@dataclass
class GitHubConfig:
    """GitHub authentication and repository settings."""
    username: str = "Shineii86"
    token: str = ""
    email: str = ""          # auto-detected from token if empty
    repo_name: str = "commit-graph-demo"
    force_push: bool = True


@dataclass
class CustomTextConfig:
    """Settings for custom text drawing mode."""
    enabled: bool = False
    text: str = "HELLO"
    start_offset_weeks: int = 0
    commits_per_pixel: int = 3


@dataclass
class RandomPatternConfig:
    """Settings for random commit pattern mode."""
    start_date: str = "2026-04-01"
    end_date: str = "2026-04-15"
    min_commits_start: int = 0
    max_commits_start: int = 5
    min_commits_end: int = 5
    max_commits_end: int = 10


@dataclass
class GeneralConfig:
    """General runtime settings."""
    dry_run: bool = False
    intermediate_push_days: int = 0


@dataclass
class AppConfig:
    """Top-level configuration container."""
    github: GitHubConfig = field(default_factory=GitHubConfig)
    custom_text: CustomTextConfig = field(default_factory=CustomTextConfig)
    random_pattern: RandomPatternConfig = field(default_factory=RandomPatternConfig)
    general: GeneralConfig = field(default_factory=GeneralConfig)
    start_date: str = "2026-04-01"  # shared between modes

    def validate(self) -> list[str]:
        """
        Validate configuration and return a list of error messages.
        Empty list = valid.
        """
        errors = []

        if not self.github.token.strip():
            errors.append("GITHUB_TOKEN is required.")
        if not self.github.username.strip():
            errors.append("GITHUB_USERNAME is required.")
        if not self.github.repo_name.strip():
            errors.append("REPO_NAME is required.")

        if self.custom_text.enabled:
            if not self.custom_text.text.strip():
                errors.append("CUSTOM_TEXT cannot be empty when custom text mode is enabled.")
            if self.custom_text.commits_per_pixel < 1:
                errors.append("COMMITS_PER_PIXEL must be at least 1.")
        else:
            if not self.random_pattern.start_date.strip():
                errors.append("START_DATE is required for random pattern mode.")
            if not self.random_pattern.end_date.strip():
                errors.append("END_DATE is required for random pattern mode.")

        if self.general.intermediate_push_days < 0:
            errors.append("INTERMEDIATE_PUSH_DAYS cannot be negative.")

        return errors
