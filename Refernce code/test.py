from pywinauto.application import Application
from pywinauto import keyboard
from mybillbookbase import mybillbookbase
import time
import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook


app=mybillbookbase()
app.menu_parties()
app.waittillload()
app.biotechindustries()
app.waittillload()
app.transactionbutton()
#app.waittillload()
app.listofheader()
app.waittillload()
app.waittillload()
app.listofdata()
#app.screenshot5()
#app.waittillload()
app.closingwindow()




#app.menu_parties()
#app.waittillload()

#app.printidentifiers()
#app.screenshot()

#app.waittillload()
#app.biotechindustries()
#app.waittillload()
#app.transactionbutton()
#app.waittillload()
#app.listofheader()
#app.waittillload()
#app.waittillload()
#app.listofdata()
#app.waittillload()
#app.printidentifiers()
# child_window(title="2023-08-29", control_type="DataItem")
#app.bulkimportbutton()
#app.waittillload()
#app.uploadpartybutton()
#app.waittillload()
#app.selectinginvoiceuser()
#app.waittillload()
#app.clickingdeletebutton()
#app.waittillload()
#app.clickingyes_deletebutton()
#app.closingthe_errormsg()
#






#app.csi()
#app.waittillload()
#app.addparty()
#app.waittillload()
#app.csi_selectingparty()
#app.waittillload()
#app.csi_selectingdate()
#app.waittillload()

#app.csi_modifyingdate()
#app.csi_createitem()
#app.waittillload()
#app.csi_serviceradiobutton()
#app.csi_itemname()
#app.csi_salesprice()
#app.csi_savebutton()
#app.waittillload()
#app.csi_addfromsampleitem()
#app.waittillload()
#app.csi_donebutton()
#app.waittillload()
#app.csi_downkey()
#app.csi_scrolldownpage()
#app.csi_markasfullypaidcheckbox()
#app.waittillload()
#app.csi_scrolluppage()
#app.waittillload()
#app.waittillload()
#app.csi_formsavebutton()
#app.waittillload()
#app.printidentifiers()









#app.menu_parties()
#app.waittillload()

#app.selectingpartyfordelete()
#app.waittillload()
#app.clickingdeletebutton()
#app.waittillload()

#app.clickingyes_deletebutton()


#app.waittillload()
#app.reportmenu()
#app.waittillload()
#app.balancesheet()
#time.sleep(5)
#app.additemincurrentasset()
#app.waittillload()
#app.downloadexcelsheetfrombalancesheet()
#app.waittillload()
#app.readdatafromexcelafterdownload()





