from pywinauto.application import Application
from pywinauto import keyboard
from mybillbookbase import mybillbookbase
import tc001data



def test_tc001():

 app=mybillbookbase()
 app.clickingcreatesalesinvoice()
 app.clickingdropdown()
 app.clickingparties()
 app.partynameinput(tc001data.name)
 #app.mobilenumber(tc001data.mn)