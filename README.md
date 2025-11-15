# Autonomous-Navigation-System-using-Camera-and-RP-Lidar

## Overview
This project focuses on **object detection and automated traversing** for autonomous vehicles by integrating **camera vision** and **RPLiDAR** sensor data. 

The aim is to enable a vehicle to understand its surroundings, detect obstacles, and navigate safely without human intervention.  

This Project idea was an inspiration from the masters session which was taken by Sir. Raghunandan M S

## Table of Contents

* [What is this?](#what-is-this)
* [Goal of this project](#goal-of-this-project)
* [Problem Statement](#problem-statement)
* [Requirements](#requirements)
* [Project Lifecycle (As per AIML Methodology)](#project-lifecycle-as-per-aiml-methodology)
* [How to use](#how-to-use)
* [Tools & Technologies](#tools--technologies)
* [Features](#features)
* [License](#license)
* [Evaluation Metrics](#evaluation-metrics)
* [Future Improvements](#future-improvements)
* [References](#references)
* [Author](#author)



## What is this?
This is a sample code collection about Autonomous Navigation System using USB-Camera and RPLidar. Each source code are implemented with Python to help your understanding.

You can fork this repository and use for studying, education or work freely.



## Goal of this project
- To implement **real-time object detection** using deep learning models (YOLOv8/SSD/CNN).
- To integrate **LiDAR data** for accurate obstacle distance measurement and mapping.
- To achieve **autonomous navigation** based on environmental understanding.
- To create a system deployable on **edge devices** like Raspberry Pi or Jetson Nano.



## Problem Statement
> "How can we enable a vehicle to detect and avoid obstacles in real-time using computer vision and LiDAR sensors for safe autonomous navigation?"

This problem focuses on the **Automotive domain**, specifically **object detection and situational awareness** for self-driving or semi-autonomous systems.



## Requirements
Before we begin, This project requires two hardware devices:
1. RpLidar(The version I used is A1M8)
2. USB Camera(Any webcam is fine for testing)

Detailed steps on how to use this repo is given in here: * [How to use](#how-to-use) 

Please satisfy with the following requirements on native or VM Linux in advance.  
For running each sample codes:  
- * [Python 3.13.x](https://www.python.org/)
- For other dependencies or packages(eg: numPy, SciPy, etc. ), **Inside an python environment**(Create it before running the below code) Use the below Code:
    ```bash
    pip install -r requirements.txt
    ```
  This will install all the packages that is necessary for this project.

- Use VS Code Editor : * [VS Code](https://code.visualstudio.com/)
  or any other editor for environment set-up



## Project Lifecycle (As per AIML Methodology)
### 1. **Problem Understanding**
- Analyze navigation and safety challenges in autonomous systems.
- Define functional goals: detection, localization, and path adjustment.

### 2. **Data Collection & Preparation**
- Collect camera image/video datasets (e.g., COCO or custom road scenes).
- Gather point cloud data from **RPLiDAR**.
- Clean and synchronize sensor data streams for alignment.
- Preprocess images (resizing, normalization) and LiDAR scans.

### 3. **Model Building**
- Use **YOLOv8 / SSD** for real-time object detection from camera feed.
- Fuse LiDAR distance data with detection coordinates for obstacle depth mapping.
- Use Python frameworks like:
  - `OpenCV`, `PyTorch`, `Ultralytics YOLO`, `rplidar`, `NumPy`, `Matplotlib`.

### 4. **Evaluation & Deployment**
- Evaluate model using **Precision**, **Recall**, and **F1-score**.
- Deploy on a local system or edge device (Jetson Nano/Raspberry Pi).
- Real-time visualization using **OpenCV** and **Matplotlib** for LiDAR overlay.

### 5. **Monitoring & Feedback**
- Record navigation performance and collision metrics.
- Retrain the detection model with new datasets for improved accuracy.



## How to use
1. **Clone this repository**
  In the git bash, use: 

    ```bash
    $ git clone https://github.com/mohan27042007/Autonomous-Navigation-System-using-Camera-and-RP-Lidar
    ```
    **or** 
  
  use **VS Code**: 
    settings -> Command pallet -> paste the github link -> Choose system file directory -> save the pulled file

2. **Setting up the environment for running the code**
  For this:
  -Create a V-env:(windows/macOS/Linux):
    ```bash
    python -m venv ml_env
    ```  

  -Activate the env:
    For windows:
    ```bash
    .\ml_env\Scripts\activate
    ```

    For macOS/ Linux:
    ```bash
    source ml_env/bin/activate
    ```
  
  -Upgrade pip:
    ```bash
    pip install --upgrade pip
    ```

  -Install All dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Project**

  Use the below code: (windows/macOS/Linux):

  ```bash
  python main.py
  ```
4. **Deactivate Once Done**

  ```bash
  deactivate
  ```

5. **Add star to this repository if you like it!!**



## Tools & Technologies
| Category | Tools Used |
|-----------|-------------|
| Programming | Python, Jupyter Notebook |
| ML Frameworks | TensorFlow / PyTorch / YOLO |
| Sensor Interface | RPLiDAR SDK, OpenCV |
| Visualization | Matplotlib, Seaborn |
| Deployment | Streamlit / Flask for demo interface |
| Dataset Sources | COCO, KITTI, Custom data from camera feed |



## Features
- Real-time camera-based object detection  
- Obstacle distance estimation using LiDAR  
- Path adjustment logic for navigation  
- Visualization of LiDAR and detection fusion  
- Edge-deployable lightweight system  



## License
MIT  



## Evaluation Metrics

### **A. FPS Benchmark**
| Condition | FPS (Approx) |
|----------|---------------|
| Empty scene | 16 FPS |
| With 1 object | 17-18 FPS |
| With 3–5 objects | 18-20 FPS |
| After 3 minutes(worst case) | 22-25 FPS |
| After 5 minutes(worst case) | 23-25 FPS |
| After 10 minutes(worst case) | 27 FPS |

---

### **B. Latency Benchmark (YOLO Inference Time)**
| Condition | Latency (ms) |
|-----------|--------------|
| Minimum latency | 32-40 ms |
| Average latency | 40-47 ms |
| Maximum latency | 42-50 ms |

---

### **C. LiDAR Scan Stability**
| Scan No. | Points Received | Status |
|----------|------------------|--------|
| Scan 1 | 292 | Unstable |
| Scan 2 | 351 | Stable |
| Scan 3 | 348 | Stable |
| Notes | — | Occasional packet drop due to cable sensitivity |

---

### **D. CPU & RAM Usage**
| Time | CPU Usage (%) | RAM Usage (%) |
|------|----------------|----------------|
| Start | 42% | 47% |
| After 3 minutes | 45% | 49% |
| After 5 minutes | 47% | 51% |
| After 10 minutes | 49% | 54% |

---

### **E. Overall System Stability**
| Duration | Result |
|----------|--------|
| 3-minute continuous run | Stable |
| 5-minute continuous run | Occasional frame drops |
| 10-minute continuous run | Acceptable performance / LiDAR restart required |



## Future Improvements
- Integrate **SLAM (Simultaneous Localization and Mapping)** for route planning.  
- Enable **multi-sensor fusion** (e.g., GPS, IMU).  
- Deploy with **TensorFlow Lite** for edge optimization.  



## References
- *Edunet Foundation – Practical Approach for AIML Projects (Session 1)*  
- *Ultralytics YOLO Documentation*  
- *RPLiDAR A1M8 SDK & ROS Integration Guide*  
- *OpenCV & PyTorch Official Docs*  

## Author
[Mohanarangan T R](https://github.com/mohan27042007)  
