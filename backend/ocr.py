from PIL import Image
import cv2 
import sys
import pytesseract
import argparse
import os
import json


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

uploaded_text = pytesseract.image_to_string(Image.open(filename))
uploaded_text = uploaded_text.replace('\n', '')
uploaded_text = uploaded_text.lower()
uploaded_text = uploaded_text.replace(', ', ',')
uploaded_text = uploaded_text.split(",")
os.remove(filename)

f = open('paulas_data.json')
datafile = f.read()
paulas_data = json.loads(datafile)
finalInfo = ""
for ingredient in uploaded_text:
    if (ingredient in paulas_data):
        my_info = "Ingredient: " + ingredient + '\n' + "Rating: " + paulas_data[ingredient][0]['Rating'] + '\n' + "Description: " + paulas_data[ingredient][0]['Description'] + '\n'
        finalInfo = finalInfo + my_info + '\n'

print(finalInfo)
f.close()
