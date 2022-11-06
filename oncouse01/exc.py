import openpyxl
book = openpyxl.load_workbook("sheet.py")
sheet =book.active
ceel =sheet["A1":"C3"]
ceel.value()

