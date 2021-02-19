import io
import json
import cv2
import numpy as np
import requests
img = cv2.imread(r"C:\Users\pbisht\PycharmProjects\pytesseract\pytesseract\page_1.jpg")
print(img)

height, width,_ = img.shape
# print(img.shape)


# Cutting image
roi = img[0: height, 400: width]


# Ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg",roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
              files = {"page_1.jpg": file_bytes},
              data = {"apikey": "6568259dff88957",
                      "language": "eng"})

result = result.content.decode()
result = json.loads(result)


parsed_results = result.get(result)
text_detected = parsed_results.get(parsed_results)
print(text_detected)