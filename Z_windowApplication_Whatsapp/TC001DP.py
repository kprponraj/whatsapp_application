import pandas as pd
import xlrd

#df = pd.read_excel(r'C:\Users\ponraj.kasirajan\Desktop\data.xlsx')
#print(df)

excel_workbook = xlrd.open_workbook(r'C:\Users\ponraj.kasirajan\PycharmProjects\pythonProject\TestData\TC001.xls')
excel_worksheet = excel_workbook.sheet_by_index(0)
up_name = excel_worksheet.cell_value(1, 1)
up_backend = excel_worksheet.cell_value(1, 2)
up_title = excel_worksheet.cell_value(1, 3)
up_text = excel_worksheet.cell_value(1, 4)
up_groupname = excel_worksheet.cell_value(1, 5)
up_dpmsg = excel_worksheet.cell_value(1, 6)
up_contactpersonname = excel_worksheet.cell_value(1, 7)
up_msgforarun = excel_worksheet.cell_value(1, 8)
up_profilepicname = excel_worksheet.cell_value(1, 9)
up_audiocallname = excel_worksheet.cell_value(1, 10)
