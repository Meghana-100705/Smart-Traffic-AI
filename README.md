# 🚦 AI-Powered Traffic Queue Analysis using Video Analytics

### Hackathon MVP – First Round Online Screening

This project demonstrates an AI-based traffic analysis system that uses computer vision to detect vehicles from traffic video footage and estimate queue length near traffic signals.

---

## 👥 Team Information

 Malireddy Meghana – AI / Computer Vision (YOLO, OpenCV)
 Kalingiri Vineela – Frontend Dashboard (HTML, CSS, JavaScript)
 Shaik Husna Tayyaba – System Architecture & Integration
 kummari Sindhu – Documentation & Presentation

---

## 🔍 Problem Statement
Urban intersections in India suffer from traffic congestion due to inefficient signal utilization and lack of real-time traffic analytics. Although CCTV cameras are widely deployed, most video feeds are used only for passive monitoring rather than intelligent analysis.

---

## 💡 Proposed Solution
We propose an AI-powered traffic monitoring system that analyzes traffic video footage to:
- Detect vehicles automatically using deep learning
- Estimate vehicle queue length near traffic signal stop-lines
- Provide visual feedback through annotated video output

The system is designed as a modular MVP that can be extended for advanced traffic analytics and violation detection.

---

## 🧠 Current Technical Implementation
The current implementation focuses on **vehicle detection and queue length estimation**.

### Vehicle Detection
- Uses **YOLOv8**, a deep learning–based object detection model
- Detects vehicles such as cars, bikes, buses, and trucks in each video frame

### Queue Length Estimation
- A **Region of Interest (ROI)** is defined near the traffic signal
- Vehicles whose center points fall within the ROI are counted
- The total count represents the **queue length**

This approach is **rule-based and explainable**, making it easy to validate visually.

---

## 🖥️ System Architecture (Current MVP)

Traffic Video
↓
YOLOv8 Vehicle Detection (Python)
↓
ROI-Based Queue Counting
↓
Annotated Video Output (OpenCV)


---

## 📊 Output Visualization
- Bounding boxes drawn around detected vehicles
- Queue region highlighted using a rectangular ROI
- Queue length displayed directly on the video frame

Visualization is handled using **OpenCV**.

---

## ⚙️ Technologies Used (Current)
- **Programming Language:** Python  
- **Object Detection:** YOLOv8 (Ultralytics)  
- **Computer Vision & Video Processing:** OpenCV  

---

## ▶️ How to Run the Project
```bash
pip install -r requirements.txt
python backend/main.py

##🚀 Future Enhancements

The following features are planned for future development:

Multi-object tracking (DeepSORT / ByteTrack)

Queue density estimation

Traffic rule violation detection (red-light jumping, rash driving)

Web-based dashboard for real-time analytics

Live camera feed integration

Smart traffic signal optimization
