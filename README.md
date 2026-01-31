# AI-Powered Traffic Queue Analysis Using Video Analytics
## Hackathon MVP – First Round Online Screening

This project presents an AI-based traffic analysis system that uses computer vision to detect vehicles from traffic video footage and estimate queue length near traffic signals. The solution demonstrates how existing CCTV infrastructure can be leveraged for intelligent traffic monitoring.

---

## Team Information

- **Malireddy Meghana** – AI / Computer Vision (YOLO, OpenCV)  
- **Kalingiri Vineela** – Frontend Dashboard (HTML, CSS, JavaScript)  
- **Shaik Husna Tayyaba** – System Architecture & Integration  
- **Kummari Sindhu** – Documentation & Presentation  

---

## Problem Statement

Urban intersections in India suffer from traffic congestion due to inefficient signal utilization and the lack of real-time traffic analytics. Although CCTV cameras are widely deployed, most video feeds are used only for passive monitoring rather than intelligent analysis.

---

## Proposed Solution

An AI-powered traffic monitoring system that:
- Automatically detects vehicles using deep learning  
- Estimates vehicle queue length near traffic signal stop-lines  
- Provides real-time visual feedback through annotated video output  

The system is designed as a modular MVP that can be extended for advanced traffic analytics and violation detection.

---

## Technical Implementation (Current MVP)

### Vehicle Detection
- Uses **YOLOv8** for real-time object detection  
- Detects cars, bikes, buses, and trucks in each video frame  

### Queue Length Estimation
- A **Region of Interest (ROI)** is defined near the traffic signal  
- Vehicles whose center points fall within the ROI are counted  
- The total count represents the queue length  

This approach is rule-based, transparent, and easy to validate visually.

---

## System Architecture

Traffic Video
↓
YOLOv8 Vehicle Detection (Python)
↓
ROI-Based Queue Counting
↓
Annotated Video Output (OpenCV)

---

## Output Visualization

- Bounding boxes drawn around detected vehicles  
- Queue region highlighted using a rectangular ROI  
- Queue length displayed directly on the video frame  

---

## Technologies Used

- **Python**  
- **YOLOv8 (Ultralytics)**  
- **OpenCV**


Scope of Current MVP

This submission focuses on vehicle detection and queue length estimation using pre-recorded traffic video. Advanced features such as tracking, violation detection, and dashboard integration are planned for future development.