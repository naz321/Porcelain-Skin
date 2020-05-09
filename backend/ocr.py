from PIL import Image
import cv2 
import sys
import pytesseract
import argparse
import os



ap = argparse.ArgumentParser()
# --image is the path to the image we are sending through the OCR system
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# converting the image from its current color space to a gray color space
src = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# TODO: spelling checks (e.g. "l is often unidentified")
# TODO: zoom in images before processing them as results are more accurate when text is bigger
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, src)

text = pytesseract.image_to_string(Image.open(filename))
text = text.replace('\n', '')
text = text.split(",")

os.remove(filename)
print(text)

