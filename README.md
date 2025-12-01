# Digital Forensics Toolkit

## 🔍 Overview

This project is a simple **Digital Forensics Toolkit** built in Python.  
It is designed to simulate basic forensic activities such as:

- Collecting system information  
- Calculating file hashes (MD5, SHA1, SHA256)  
- Extracting image metadata (EXIF)  
- Parsing log files into a readable timeline  

The toolkit is intended for learning and demonstration purposes in a controlled environment.

---

## 🛠 Tools & Technologies

- Python 3
- Standard Library (os, hashlib, datetime, pathlib)
- `exifread` (for EXIF metadata extraction)

---

## 📂 Project Structure

```text
DigitalForensicsToolkit/
 ├── evidence/
 │    ├── sample.log
 │    └── sample_image.jpg
 ├── scripts/
 │    ├── system_info.py
 │    ├── hashing.py
 │    ├── metadata.py
 │    ├── log_parser.py
 │    └── forensics_toolkit.py
 ├── reports/
 ├── images/
 │    ├── menu.png
 │    ├── hash_output.png
 │    └── log_output.png
 └── README.md
⚙️ Features

1️⃣ System Information Collection
	•	Captures hostname, IP, OS, CPU, Python version, and timestamp.
	•	Can save output as a JSON report.

2️⃣ File Hashing
	•	Calculates MD5, SHA1, and SHA256 hashes of any given file.
	•	Useful for integrity verification and evidence handling.

3️⃣ Image Metadata Extraction
	•	Uses exifread to extract EXIF metadata from image files.
	•	Helps in analyzing camera details, timestamps, etc. (if present).

4️⃣ Log Parsing
	•	Parses simple log files and creates a readable event timeline.

How to Run
	1.	Create and activate virtual environment:
python3 -m venv venv
source venv/bin/activate
pip install exifread

	2.	Run the toolkit:
cd scripts
python forensics_toolkit.py

	3.	Follow the on-screen menu and provide paths like:

	•	../evidence/sample.log
	•	../evidence/sample_image.jpg
📚 Skills Demonstrated
	•	Basic digital forensics concepts
	•	Evidence handling & integrity (hashing)
	•	Metadata analysis
	•	Log analysis & timeline reconstruction
	•	Python scripting & modular design

⸻

👤 Author

Sarthak Singh Dangi
BSc (Hons) Forensic Science
Intern – CodeCTe Technologies
