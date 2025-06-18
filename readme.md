# 🎨 Color Tracking with OpenCV

This project detects a specific color (e.g. blue) in real-time using your webcam, and tracks the object using contour detection.

## 🔧 Tools Used
- Python
- OpenCV
- NumPy
- HSV color filtering
- Contour detection


## 🚀 How It Works
- Converts webcam frame from BGR to HSV
- Filters specific color range using `cv2.inRange()`
- Finds contours and draws bounding boxes

## 📦 Installation
```bash
pip install opencv-python numpy
