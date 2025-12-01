from pathlib import Path
from datetime import datetime

def parse_log_file(log_path):
    log_file = Path(log_path)
    if not log_file.is_file():
        raise FileNotFoundError(f"Log file not found: {log_path}")

    events = []
    with log_file.open("r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Example: 2025-11-30 10:15:23 user=alice action=login ip=192...
            parts = line.split(" ", 2)
            timestamp_str = f"{parts[0]} {parts[1]}"
            rest = parts[2] if len(parts) > 2 else ""
            try:
                ts = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue

            events.append({"timestamp": ts, "details": rest})

    return events

if __name__ == "__main__":
    path = input("Enter log file path: ")
    events = parse_log_file(path)
    for e in events:
        print(f"{e['timestamp']} -> {e['details']}")
