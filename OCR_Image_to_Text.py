#! python3

import cv2
import numpy as np
import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe")

src_path = os.path.join("C:\\", "users", "ccholon", "documents", "python", "pytesseract_ocr")

img_path = src_path + "\\test.png"

# Read image with OpenCV
img = cv2.imread(img_path)

# Convert image to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply dilation and erosion to remove some noise
# kernel = np.ones((1, 1), np.uint8)
# img = cv2.dilate(img, kernel, iterations=1)
# img = cv2.erode(img, kernel, iterations=1)

cv2.imwrite(src_path + "\\removed_noise.png", img)

# Apply threshold to get image with only black and white
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite(src_path + "\\thres.png", img)

# Run image through OCR
result = pytesseract.image_to_string(Image.open(src_path + "\\thres.png"))

print(result)