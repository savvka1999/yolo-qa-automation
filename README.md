# 🚗 YOLO QA Automation

[![YOLO QA Tests](https://github.com/savvka1999/yolo-qa-automation/actions/workflows/test.yml/badge.svg)](https://github.com/savvka1999/yolo-qa-automation/actions/workflows/test.yml)

Automated testing framework for Computer Vision (YOLO) models using Python, Pytest, Docker, and CI/CD.

## 📖 About the Project

This project is an End-to-End (E2E) testing framework designed to validate the quality of neural network object detectors. 
It automatically runs inference on video files, compares the performance of two model versions (lightweight vs. heavy), and calculates key quality metrics.

**Key Features:**
*   Real YOLO (Ultralytics) inference on video files.
*   Model comparison (e.g., `yolo11n` vs. `yolo11s`).
*   Calculation of **Precision**, **Recall**, and **IoU** (Intersection over Union) metrics.
*   Counting of **True Positives**, **False Positives**, and **False Negatives**.
*   Real-time visualization of detections (bounding boxes) using OpenCV.
*   Fully isolated environment via **Docker**.
*   Automated test execution in the cloud via **GitHub Actions (CI/CD)**.

## 🛠 Tech Stack

*   **Language:** Python 3.12
*   **Testing:** Pytest
*   **Computer Vision:** Ultralytics (YOLO), OpenCV
*   **Containerization:** Docker
*   **CI/CD:** GitHub Actions

## 📂 Project Structure

*   `real_model.py` — Script to run YOLO inference and save results to JSON.
*   `test_compare_models.py` — Main test that runs two models and compares them via IoU.
*   `test_iou_math.py` — Module with the mathematical IoU calculation function.
*   `visualize_video.py` — Script for visual inspection of detections on video.
*   `Dockerfile` — Instructions for building the Docker image.
*   `.github/workflows/test.yml` — CI/CD pipeline configuration for GitHub Actions.

## 🚀 How to Run Locally

1. Ensure you have Python 3.12 installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
Run the tests:

bash
pytest test_compare_models.py -s

🐳 How to Run in Docker
Build the image:

bash
docker build -t qa-yolo-tests .
Run the container with tests:

bash
docker run --rm qa-yolo-tests

⚙️ CI/CD
The project is configured to automatically run tests on every push to the main (or master) branch.
Build results and logs are available in the Actions tab on GitHub.

Author: Savva Sidorov