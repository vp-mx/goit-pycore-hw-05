import re
import sys
from collections import Counter
from pathlib import Path


LOG_LINE_PATTERN = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}:\d{2})\s+(?P<level>\w+)\s+(?P<message>.+)"
)


def parse_logs_from_file(file_path: "Path") -> list[dict[str, str]]:
    """Loads logs from a file and parses them into a list of LogEntry named tuples."""

    if not file_path.exists() or not file_path.is_file():
        print(f"Error: File '{file_path}' not found or not a file.")
        sys.exit(1)
    with open(file_path, "r") as file:
        lines = file.read()

    matches = LOG_LINE_PATTERN.finditer(lines)
    return [match.groupdict() for match in matches]


def display_log_counts(counter_dict: dict[str, int]) -> None:
    """Prints the log counts in a formatted table using built-in methods."""

    records = [f"{'Level':<10} | {'Count':<5}", "-" * 18]
    records.extend(f"{level:<10} | {count:<5}" for level, count in counter_dict.items())
    print("\n".join(records))


def print_logs_with_level(logs: list[dict[str, str]], level: str) -> None:
    """Prints logs with the specified log level."""

    filtered_logs = list(filter(lambda log: log["level"] == level, logs))
    records = [f"\nDetails for log level '{level}':"]
    records.extend(f"{log['date']} {log['time']} - {log['message']}" for log in filtered_logs)
    print("\n".join(records))


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file_path> [log_level]")
        sys.exit(1)

    log_file_path = Path(__file__).parent / sys.argv[1]
    log_level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    logs = parse_logs_from_file(log_file_path)
    log_counts = Counter(log["level"] for log in logs)
    display_log_counts(log_counts)

    if log_level:
        print_logs_with_level(logs, log_level)


if __name__ == "__main__":
    main()
