import json
from pathlib import Path

from system_info import get_system_info
from hashing import calculate_hashes
from metadata import extract_metadata
from log_parser import parse_log_file


def main_menu():
    while True:
        print("\n=== Digital Forensics Toolkit ===")
        print("1. Collect System Information")
        print("2. Calculate File Hashes")
        print("3. Extract Image Metadata")
        print("4. Parse Log File")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            handle_system_info()
        elif choice == "2":
            handle_hashes()
        elif choice == "3":
            handle_metadata()
        elif choice == "4":
            handle_log_parsing()
        elif choice == "5":
            print("Exiting toolkit.")
            break
        else:
            print("Invalid choice. Try again.")


def handle_system_info():
    info = get_system_info()
    print("\n[System Information]")
    for k, v in info.items():
        print(f"{k}: {v}")

    save = input("Save to JSON report? (y/n): ").strip().lower()
    if save == "y":
        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)
        out_file = reports_dir / "system_info.json"
        out_file.write_text(json.dumps(info, indent=2))
        print(f"Saved to {out_file}")


def handle_hashes():
    path = input("Enter file path to hash (e.g., evidence/sample.log): ").strip()
    try:
        hashes = calculate_hashes(path)
    except FileNotFoundError as e:
        print(e)
        return

    print("\n[File Hashes]")
    for algo, h in hashes.items():
        print(f"{algo}: {h}")


def handle_metadata():
    path = input("Enter image path (e.g., evidence/sample_image.jpg): ").strip()
    try:
        meta = extract_metadata(path)
    except FileNotFoundError as e:
        print(e)
        return

    if not meta:
        print("No EXIF metadata found.")
    else:
        print("\n[Image Metadata]")
        for k, v in meta.items():
            print(f"{k}: {v}")


def handle_log_parsing():
    path = input("Enter log file path (e.g., evidence/sample.log): ").strip()
    try:
        events = parse_log_file(path)
    except FileNotFoundError as e:
        print(e)
        return

    print("\n[Parsed Log Events]")
    for e in events:
        print(f"{e['timestamp']} -> {e['details']}")


if __name__ == "__main__":
    # Ensure imports work when running from scripts/
    import sys
    from pathlib import Path as _Path

    sys.path.append(str(_Path(__file__).resolve().parent))
    main_menu()
