# Autonomous-Navigation-System-using-Camera-and-RP-Lidar

## 📘 Overview
This project focuses on **object detection and automated traversing** for autonomous vehicles by integrating **camera vision** and **RPLiDAR** sensor data. The aim is to enable a vehicle to understand its surroundings, detect obstacles, and navigate safely without human intervention.  

This Project idea was an inspiration from the masters session which was taken by Sir. Raghunandan M S



## 🎯 Objectives
- To implement **real-time object detection** using deep learning models (YOLOv8/SSD/CNN).
- To integrate **LiDAR data** for accurate obstacle distance measurement and mapping.
- To achieve **autonomous navigation** based on environmental understanding.
- To create a system deployable on **edge devices** like Raspberry Pi or Jetson Nano.



## 🧩 Problem Statement
> "How can we enable a vehicle to detect and avoid obstacles in real-time using computer vision and LiDAR sensors for safe autonomous navigation?"

This problem focuses on the **Automotive domain**, specifically **object detection and situational awareness** for self-driving or semi-autonomous systems.



## 🔄 Project Lifecycle (As per AIML Methodology)
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



## 🧠 Tools & Technologies
| Category | Tools Used |
|-----------|-------------|
| Programming | Python, Jupyter Notebook |
| ML Frameworks | TensorFlow / PyTorch / YOLO |
| Sensor Interface | RPLiDAR SDK, OpenCV |
| Visualization | Matplotlib, Seaborn |
| Deployment | Streamlit / Flask for demo interface |
| Dataset Sources | COCO, KITTI, Custom data from camera feed |



## ⚙️ Features
- Real-time camera-based object detection  
- Obstacle distance estimation using LiDAR  
- Path adjustment logic for navigation  
- Visualization of LiDAR and detection fusion  
- Edge-deployable lightweight system  



## 📊 Evaluation Metrics
- **Precision & Recall** – Object detection accuracy  
- **F1 Score** – Balance between detection accuracy and false positives  
- **Latency** – Real-time inference speed  
- **Collision Rate Reduction** – Safety metric for traversing  



## 🧱 Future Improvements
- Integrate **SLAM (Simultaneous Localization and Mapping)** for route planning.  
- Enable **multi-sensor fusion** (e.g., GPS, IMU).  
- Deploy with **TensorFlow Lite** for edge optimization.  



## 🧩 References
- *Edunet Foundation – Practical Approach for AIML Projects (Session 1)*  
- *Ultralytics YOLO Documentation*  
- *RPLiDAR A1M8 SDK & ROS Integration Guide*  
- *OpenCV & PyTorch Official Docs*  


