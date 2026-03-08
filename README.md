# Clockwork

## Micro Frame Video Forensic Extractor

Clockwork is a Python-based digital forensics tool designed to extract micro-level frames from video files for detailed investigation and analysis.

The tool allows investigators, researchers, and security analysts to capture frames at custom time intervals (seconds or milliseconds) to analyze events that occur too quickly for normal video playback.

Clockwork can assist in video evidence analysis, CCTV investigation, and frame-by-frame forensic examination.

---

## Features

* Extract frames from video files
* Custom frame extraction interval
* Timestamp-based frame naming
* Automatic output directory creation
* Fast processing using OpenCV
* Lightweight command-line interface
* Suitable for forensic and research workflows

---

## Use Cases

Clockwork can be used for:

* Digital forensics investigations
* CCTV footage analysis
* Video evidence examination
* Motion and event analysis
* Security research
* Video tampering analysis
* Frame-by-frame investigation

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Saksham122004/Clockwork.git
cd Clockwork
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

Python 3.8 or higher

Required Python packages:

* opencv-python
* numpy
* tqdm

---

## Usage

Basic syntax:

```bash
python Clockwork.py <video_file> -i <interval> -o <output_folder>
```

Example:

```bash
python Clockwork.py video.mp4 -i 0.01 -o frames
```

---

## Arguments

| Argument        | Description                          |
| --------------- | ------------------------------------ |
| video           | Path to input video file             |
| -i / --interval | Frame extraction interval in seconds |
| -o / --output   | Directory where frames will be saved |

---

## Output Example

```
frames/
 ├── frame_000001_0.000000s.jpg
 ├── frame_000002_0.010000s.jpg
 ├── frame_000003_0.020000s.jpg
 ├── frame_000004_0.030000s.jpg
```

Each extracted frame contains a timestamp in the filename indicating the exact moment captured in the video.

---

## Disclaimer

This project is intended for educational purposes, digital forensics, and authorized security research only.

Users are responsible for ensuring that the use of this software complies with all applicable laws and regulations.





