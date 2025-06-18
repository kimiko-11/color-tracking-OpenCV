import cv2
import matplotlib.pyplot as plt

# Load an image in BGR format (OpenCV default)
img_bgr = cv2.imread("C:/Users/Kimaya/OneDrive/Desktop/red_shirt.webp")  # Replace with your image name
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

# Show all 3 using matplotlib (which expects RGB)
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img_bgr)  # This will show incorrect colors
plt.title("BGR (OpenCV default)")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(img_rgb)  # Correct colors
plt.title("RGB (for display)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(img_hsv)
plt.title("HSV (color detection)")
plt.axis("off")

plt.tight_layout()
plt.show()
