import win32com.client
import os

word = win32com.client.Dispatch("word.Application")
word.visible = 0

doc_pdf = r"C:\Users\pbisht\VScode project OCR\Assignment 3\31. 1260993H Kaiser Fontana Medical Center PPE 1-29-21 Hotel.pdf"

input_file = os.path.abspath(doc_pdf)

wb = word.Documents.Open(input_file)
# print(wb)
output_file = os.path.abspath(doc_pdf + ".docx".format())
wb.saveAs2(output_file, FileFormat=16)
# print("file converted")
wb.close()
word.Quit()
