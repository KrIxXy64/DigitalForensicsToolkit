import hashlib
from pathlib import Path

def calculate_hashes(file_path):
    file = Path(file_path)
    if not file.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    hashes = {
        "md5": hashlib.md5(),
        "sha1": hashlib.sha1(),
        "sha256": hashlib.sha256(),
    }

    with file.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            for h in hashes.values():
                h.update(chunk)

    return {name: h.hexdigest() for name, h in hashes.items()}

if __name__ == "__main__":
    path = input("Enter file path to hash: ")
    result = calculate_hashes(path)
    for algo, h in result.items():
        print(f"{algo}: {h}")
