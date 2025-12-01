from pathlib import Path
import exifread

def extract_metadata(image_path):
    image_file = Path(image_path)
    if not image_file.is_file():
        raise FileNotFoundError(f"File not found: {image_path}")

    metadata = {}

    with image_file.open("rb") as f:
        tags = exifread.process_file(f, details=False)

    for tag in tags.keys():
        metadata[str(tag)] = str(tags[tag])

    return metadata

if __name__ == "__main__":
    path = input("Enter image path: ")
    data = extract_metadata(path)
    if not data:
        print("No EXIF metadata found.")
    else:
        for k, v in data.items():
            print(f"{k}: {v}")
