from pywinauto.application import Application
from pywinauto import keyboard
from mybillbookbase import mybillbookbase
import tc001data
import logging
import pytest


def test_creataparty():
 logging.info("Test case starting...")
 app=mybillbookbase()
 #app.clickingcreatesalesinvoice()
 app.clickingdropdown()
 app.clickingparties()
 app.partynameinput(tc001data.name)
 app.mobilenumber(tc001data.mn)
 app.emailinputbox(tc001data.email)
 app.openingbalancefield(tc001data.amount)
 app.partycategory()
 app.createcategory()
 app.createcategoryname(tc001data.categoryname)
 app.savecategoryname()
 app.gstnumberinputbox(tc001data.gstnumber)
 app.pannumberinputbox(tc001data.pannumber)
 app.billingaddresspopup()
 app.billingaddress_streetname(tc001data.address)
 app.billingaddress_state(tc001data.state)
 app.billingaddress_pincode(tc001data.pincode)
 app.billingaddress_city(tc001data.city)
 app.billingaddress_savebutton()
 #app.categorysuccessmsgcloseicon()
 app.partysavebutton()
 app.screenshot1()
 app.menu_parties()
 app.getnameandverifyname(tc001data.name)
 app.getandverifycategory(tc001data.categoryname)
 app.searchpartbyname(tc001data.name)
 app.waittillload()
 app.closingwindow()
 logging.info("Test case passed!")

@pytest.mark.xfail
def test_creatingaduplicateparty():
 logging.info("Test case starting...")
 app = mybillbookbase()
 #app.clickingcreatesalesinvoice()
 app.clickingdropdown()
 app.clickingparties()
 app.partynameinput(tc001data.name)
 app.mobilenumber(tc001data.mn)
 app.emailinputbox(tc001data.email)
 app.openingbalancefield(tc001data.amount)
 app.partycategory()
 app.createcategory()
 app.createcategoryname(tc001data.categoryname)
 app.savecategoryname()
 app.screenshot2()
 app.gstnumberinputbox(tc001data.gstnumber)
 app.pannumberinputbox(tc001data.pannumber)
 app.billingaddresspopup()
 app.billingaddress_streetname(tc001data.address)
 app.billingaddress_state(tc001data.state)
 app.billingaddress_pincode(tc001data.pincode)
 app.billingaddress_city(tc001data.city)
 app.billingaddress_savebutton()
 # app.categorysuccessmsgcloseicon()
 app.partysavebutton()
 app.menu_parties()
 app.getnameandverifyname(tc001data.name)
 app.getandverifycategory(tc001data.categoryname)
 app.searchpartbyname(tc001data.name)
 app.closingwindow()
 logging.info("Test case passed!")
 assert False


def test_deleteaparty():
  logging.info("Test case starting...")
  app = mybillbookbase()
  app.menu_parties()
  app.waittillload()
  app.selectingpartyfordelete()
  app.waittillload()
  app.clickingdeletebutton()
  app.waittillload()
  app.clickingyes_deletebutton()
  app.screenshot3()
  app.waittillload()
  app.closingwindow()
  logging.info("Test case passed!")

def test_createsalesinvoice():
 logging.info("Test case starting...")
 app = mybillbookbase()
 app.csi()
 app.waittillload()
 app.addparty()
 app.waittillload()
 app.csi_selectingparty()
 app.waittillload()
 app.csi_selectingdate()
 app.waittillload()
 app.csi_modifyingdate()
 app.csi_createitem()
 app.waittillload()
 app.csi_serviceradiobutton()
 app.csi_itemname()
 app.csi_salesprice()
 app.csi_savebutton()
 app.waittillload()
 app.waittillload()
 app.csi_formsavebutton()
 app.screenshot4()
 app.waittillload()
 app.closingwindow()
 logging.info("Test case passed!")

def test_gettingtableofdatainexcelsheet():
 logging.info("Test case starting...")
 app = mybillbookbase()
 app.menu_parties()
 app.waittillload()
 app.biotechindustries()
 app.waittillload()
 app.transactionbutton()
 # app.waittillload()
 app.listofheader()
 app.waittillload()
 app.waittillload()
 app.listofdata()
 #app.screenshot5()
 #app.waittillload()
 app.closingwindow()
 logging.info("Test case passed!")

def test_deleteapartywithsalesinvoice():
 logging.info("Test case starting...")
 app = mybillbookbase()
 app.menu_parties()
 app.waittillload()
 #app.selectingpartyfordelete()
 app.selectinginvoiceuser()
 app.waittillload()
 app.clickingdeletebutton()
 app.waittillload()
 app.clickingyes_deletebutton()
 app.screenshot6()
 app.closingthe_errormsg()
 app.waittillload()
 app.closingwindow()
 logging.info("Test case passed!")

def test_downloadexcelsheet():
 logging.info("Test case starting...")
 app = mybillbookbase()
 app.waittillload()
 app.reportmenu()
 app.waittillload()
 app.balancesheet()
 app.waittillload()
 app.downloadexcelsheetfrombalancesheet()
 app.screenshot7()
 app.waittillload()
 app.readdatafromexcelafterdownload()
 app.waittillload()
 app.closingwindow()
 logging.info("Test case passed!")

def test_downloadingexcelsheetwp():
 logging.info("Test case starting...")
 app = mybillbookbase()
 app.waittillload()
 app.reportmenu()
 app.waittillload()
 app.balancesheet()
 app.waittillload()
 app.downloadexcelsheetfrombalancesheet()
 app.waittillload()
 app.readdatafromexcelafterdownloadwp()
 app.waittillload()
 app.closingwindow()
 logging.info("Test case passed!")
