from openpyxl import load_workbook


book = load_workbook('Test.xlsx')
sheet = book['Стикеры']
 # sheet['A1'].value = 1

print(book.worksheets)
print(sheet['A1'].value)