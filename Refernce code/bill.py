from pywinauto.application import Application
from pywinauto import keyboard


app = (Application(backend='uia').start(r'C:\Users\ponraj.kasirajan\Downloads\MyBillbook-32-bit.exe').connect(title='My BillBook | Simple Billing and Inventory Software', timeout=30))



csibutton = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Create Sales Invoice", control_type="Text").wrapper_object()
csibutton.click_input()


dropdownbtn = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="open create dropdown", control_type="Image").wrapper_object()
dropdownbtn.click_input()

partybutton = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Create Party", control_type="Text").wrapper_object()
partybutton.click_input()

partynameinputbox = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Party Name*", control_type="Edit").wrapper_object()
partynameinputbox.set_text("ranjith")

mobilenumberinputbox = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Mobile Number", control_type="Edit").wrapper_object()
mobilenumberinputbox.set_text("9360465480")

emailinputbox = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Email", control_type="Edit").wrapper_object()
emailinputbox.set_text("raj2@grr.la")

openningbalance = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="0", control_type="Edit").wrapper_object()
openningbalance.set_text("10000")

#opbaldropdown = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="To Collect", auto_id="dropdownMenuButton", control_type="Group").wrapper_object()
#opbaldropdown.click_input()

#dbvaluetocollect = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="To Collect", control_type="Text").wrapper_object()
#dbvaluetocollect.click_input()

#dbvaluetopay = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="To Pay", control_type="Text").wrapper_object()
#dbvaluetopay.click_input()

#partytype = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Customer", auto_id="dropdownMenuButton", control_type="Group").wrapper_object()
#partytype.click_input()

#ddvaluecustomer = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Customer", control_type="Text").wrapper_object()
#ddvaluecustomer.click_input()

#ddvaluesupplier = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Supplier", control_type="Text").wrapper_object()
#ddvaluesupplier.click_input()

partycategory = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Select Category", auto_id="dropdownMenuButton", control_type="Group").wrapper_object()
partycategory.click_input()

#app.MyBillBookSimpleBillingAndInventorySoftware.print_control_identifiers()

createcategory = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="+ Create Category", control_type="Text",top_level_only=False).wrapper_object()
createcategory.click_input()



newcategoryname = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Enter category name", control_type="Edit").wrapper_object()
newcategoryname.set_text("sample25")

savenewcategory = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Save", control_type="Button",found_index=1).wrapper_object()
savenewcategory.click_input()


GSTinputbox = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="ex: 29XXXXX9438X1XX", control_type="Edit").wrapper_object()
GSTinputbox.set_text('29GGGGG1314R9Z0')

PANnumberinputbox = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Enter party PAN Number", control_type="Edit").wrapper_object()
PANnumberinputbox.set_text('ABCTY1234G')

enterbillingaddresspopup = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Enter billing address", control_type="Edit").wrapper_object()
enterbillingaddresspopup.click_input()

billingaddress_streetname = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Enter Street Address", auto_id="street_addr", control_type="Edit").wrapper_object()
billingaddress_streetname.set_text('No 36 Sudhama commercial buliding 4th floor T - nagar 3')

billingaddress_statesi = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Enter State", auto_id="searchInput", control_type="Edit").wrapper_object()
billingaddress_statesi.set_text("Tamil Nadu")

#billingaddress_megalaya = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Meghalaya", control_type="Text").wrapper_object()

#billingaddress_tamilnadu = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Tamil Nadu", control_type="Text").wrapper_object()
#billingaddress_tamilnadu.set_text('Tamil Nadu')

billingaddress_pincode = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Enter pin code", auto_id="pincode", control_type="Edit").wrapper_object()
billingaddress_pincode.set_text('600017')

billingaddress_city = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Enter City", auto_id="city", control_type="Edit").wrapper_object()
billingaddress_city.set_text('chennai')

billingaddress_savebutton = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Save", control_type="Button",found_index=1).wrapper_object()
billingaddress_savebutton.click_input()

#partysavebutton = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Save", control_type="Button").wrapper_object()
#partysavebutton.click_input()


creditlimitinputbox = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="0", control_type="Edit").wrapper_object()
creditlimitinputbox.set_text('10000')

categorypopupcloseicon = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="close", control_type="Text",found_index=0).wrapper_object()
categorypopupcloseicon.click_input()

partysavebutton = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Save", control_type="Button").wrapper_object()
partysavebutton.click_input()



menu_parties = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Parties", control_type="Hyperlink").wrapper_object()
menu_parties.click_input()

#app.MyBillBookSimpleBillingAndInventorySoftware.wait("enabled",timeout=20).type_keys('%{ENTER}')

#click_list = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="raj2", control_type="Text").wrapper_object()
#click_list.click_input()


#searchpartybyname = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Search party by name or number", control_type="Edit").wrapper_object()
#searchpartybyname.set_text('raj6')

#keyboard.send_keys('{ENTER}')


getname = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="ranjith", control_type="Text").wrapper_object()
textofname = getname.window_text()
print(textofname)

getcategory = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="sample25", control_type="DataItem").wrapper_object()
textofcategory = getcategory.window_text()
print(textofcategory)

getmobilenumer = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="9360465480", control_type="DataItem").wrapper_object()
textofmobilenumber = getmobilenumer.window_text()
print(textofmobilenumber )






app.MyBillBookSimpleBillingAndInventorySoftware.print_control_identifiers()

#addbutton = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="add icon", control_type="Image").wrapper_object()
#addbutton.click_input()

#window = app.MyBillBookSimpleBillingAndInventorySoftware.wrapper_object()

#app.MyBillBookSimpleBillingAndInventorySoftware.set_focus()



#def party():
    #keyboard.send_keys('%')
 #   keyboard.send_keys('+{y}')
  #  pass
#party()

#app.MyBillBookSimpleBillingAndInventorySoftware.wait('enabled').type_keys('+{y}')


#cname = app.MyBillBookSimpleBillingAndInventorySoftware.child_window(title="Jp", control_type="Text").wrapper_object()
#cname.click_input()

#app.MyBillBookSimpleBillingAndInventorySoftware.print_control_identifiers()




