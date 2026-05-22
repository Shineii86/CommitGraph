"""
Utility functions for CommitGraph.

Provides: progress bars, commit estimation, ASCII graph preview.
"""

from collections import Counter, defaultdict


def estimate_commits(pixels: list[tuple[int, int]], commits_per_pixel: int) -> tuple[int, int]:
    """
    Estimate total commits and active days for a set of pixel coordinates.

    Returns:
        (total_commits, active_days)
    """
    day_counts: Counter = Counter()
    for week, day in pixels:
        day_counts[(week, day)] += commits_per_pixel
    return sum(day_counts.values()), len(day_counts)


def progress_bar(current: int, total: int, width: int = 30) -> str:
    """
    Return a visual progress bar string.

    Example: [████████░░░░] 67%
    """
    filled = int(width * current / total) if total > 0 else 0
    bar = '█' * filled + '░' * (width - filled)
    pct = (current / total * 100) if total > 0 else 0
    return f'[{bar}] {pct:.0f}%'


def preview_graph(pixels: list[tuple[int, int]], max_week: int) -> None:
    """
    Print an ASCII preview of the contribution graph pattern.

    Args:
        pixels: List of (week, day) coordinates.
        max_week: The highest week index to display.
    """
    grid: dict[int, dict[int, bool]] = defaultdict(lambda: defaultdict(bool))
    for week, day in pixels:
        grid[week][day] = True

    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    print("\n📊 Preview of contribution graph pattern:\n")
    print('      ' + '  '.join(f'W{w}' for w in range(max_week + 1)))

    for d in range(7):
        line = f'  {days[d]} '
        for w in range(max_week + 1):
            line += '  █  ' if grid[w][d] else '  ·  '
        print(line)
    print()


def parse_date(date_str: str):
    """
    Parse a YYYY-MM-DD date string into a datetime object.

    Raises ValueError with a clear message on bad input.
    """
    from datetime import datetime
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(
            f"Invalid date format: '{date_str}'. Expected YYYY-MM-DD."
        )
