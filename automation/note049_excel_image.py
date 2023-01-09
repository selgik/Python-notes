#note049_excel_image.py
#prepare libraries and settings

from openpyxl import Workbook
wb = Workbook()
ws = wb.active


########## 1. PREPARE
from openpyxl.drawing.image import Image


########## 2. INSERT IMAGE TO THE CELL
img = Image("sample_image.png")         #let's create variable with the image file you want to insert into the cell
ws.add_image(img, "C3")                 #insert img to C3

wb.save("sample_image.xlsx")

  
