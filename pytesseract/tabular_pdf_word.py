import os

import requests
import pdfplumber

# def download_file(url):
#     local_filename = url.split('/')[-1]
#
#     with requests.get(url) as r:
#         assert r.status_code == 200, f'error, status code is {r.status_code}'
#         with open(local_filename, 'wb') as f:
#             f.write(r.content)

# return local_filename
invoice = r'C:\Users\pbisht\VScode project OCR\Assignment 3\31. 1260993H Kaiser Fontana Medical Center PPE 1-29-21 Hotel.pdf'
invoice_pdf = r'C:\Users\pbisht\VScode project OCR\Assignment 3\31. 1260993H Kaiser Fontana Medical Center PPE 1-29-21 Hotel.pdf'

with pdfplumber.open(invoice_pdf) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
    print(text)

    os.system(f'ocrmypdf {invoice_pdf} output.pdf')
with pdfplumber.open('output.pdf') as pdf:
    page = pdf.pages[0]
    text = page.extract_text(x_tolerance=2)
    print(text)

    lines = text.split('\n')
    print("lines")
# import re
# amt_re = re.compile(r'\.\d\d$')
# subt = 0
#
# for line in lines:
#     if 'SUBTOTAL' in line:
#         break
#     if amt_re.search(line):
#         subt += float(line.split()[-1].replace(',', '').replace('$', ''))
