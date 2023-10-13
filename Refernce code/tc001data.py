import pandas as pd
import xlrd

#df = pd.read_excel(r'C:\Users\ponraj.kasirajan\Desktop\data.xlsx')
#print(df)

excel_workbook = xlrd.open_workbook(r'C:\Users\ponraj.kasirajan\Desktop\TestDatas.xls')
excel_worksheet = excel_workbook.sheet_by_index(0)
name = excel_worksheet.cell_value(1, 1)
mn = '9150011384'
email = excel_worksheet.cell_value(1, 3)
amount = '15000'
categoryname = excel_worksheet.cell_value(1, 5)
gstnumber = excel_worksheet.cell_value(1, 6)
pannumber = excel_worksheet.cell_value(1, 7)
address = excel_worksheet.cell_value(1, 8)
state = excel_worksheet.cell_value(1, 9)
pincode = '600017'
city = excel_worksheet.cell_value(1, 11)



#print(name)
