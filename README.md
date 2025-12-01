# Smart Signal Detection 🚦

## 📖 Introduction
**Smart Signal Detection** is a computer vision–powered web application built with **Flask** and **OpenCV**.  
It uses a Haar Cascade classifier to detect objects (faces/signals) from a live webcam feed and dynamically updates a simulated traffic signal indicator (red/green).  

This project demonstrates how real-time vision can be integrated into traffic management systems, serving as a foundation for smarter navigation and safety solutions.

---

## 📸 Screenshots
- **Traffic Signal UI**: Displays a live webcam feed and a dynamic signal indicator.


![Traffic Signal]()


- **Signal States**: Green when no object is detected, Red when detection occurs.  


![Signal States]()

---

## 🔧 Tech Stack
- **Backend**: Flask (Python)  
- **Computer Vision**: OpenCV (Haar Cascade Classifier)  
- **Frontend**: HTML, CSS

---

## ✨ Features
- 🎥 Live webcam feed integration  
- 🚦 Dynamic traffic signal indicator (red/green)  
- ⚡ Real-time object detection using Haar Cascade  
- 🌐 Web-based interface with responsive design  

---

## 🚀 Installation & Setup

### 1. Install Libray  
-  pip install opencv-python flask 

### 2. Install haarcasde file 
- https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt2.xml
### 2. Clone the Repository
```bash
git clone https://github.com/your-username/smart-signal.git
cd smart-signal