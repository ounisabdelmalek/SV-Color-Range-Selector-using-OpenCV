# 🎨 HSV Color Range Selector using OpenCV

This simple OpenCV tool helps you interactively select and visualize a color range in the HSV (Hue, Saturation, Value) color space using trackbars. It's useful for color segmentation tasks such as object detection, image masking, and preprocessing in computer vision projects.

## 📷 Demo
![HSV Range Selector Example](![Screenshot 2025-06-25 200656](![Untitled](https://github.com/user-attachments/assets/5fd0bf3c-7e30-4a50-a23d-770056388f88)
)
![Untitled](https://github.com/user-attachments/assets/b72a16e7-f383-4b71-89e2-7251e714fe09)


)

## 🔧 Features
- Load and resize an input image.
- Convert the image to HSV color space.
- Use OpenCV trackbars to dynamically adjust:
  - Lower Hue, Saturation, Value (LH, LS, LV)
  - Upper Hue, Saturation, Value (UH, US, UV)
- See the resulting mask and segmented output in real time.
- Press `q` to quit the app.

## 🧠 How It Works
The script uses `cv2.inRange()` to create a binary mask where the HSV values are within the selected range, then applies `cv2.bitwise_and()` to extract the relevant part of the image.

## 📦 Requirements

- Python 3.x
- OpenCV
- NumPy

Install dependencies using pip:

```bash
pip install opencv-python numpy
