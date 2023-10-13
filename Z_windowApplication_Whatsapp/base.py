from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto.mouse import double_click
from pywinauto import keyboard
from pywinauto import taskbar
from pywinauto import Desktop
import time
import TC001DP




def launchingtheapplicationfromtaskbar(up_name,up_backend,up_title):
   # app_name = 'WhatsApp'
    app_name = up_name

    #desktop = Desktop(backend="uia")
    desktop = Desktop(backend=up_backend)

    taskbar = desktop.taskbar  # ["Notification chevron button"]

    app_icon = taskbar.child_window(title=app_name, control_type="Button")
    app_icon.click_input()
    time.sleep(3)

    main_window = Application(backend=up_backend).connect(title=up_title)

    time.sleep(2)
    #main_window.WhatsApp.print_control_identifiers()

pass

def printidentifiers(up_backend,up_title):
 main_window = Application(backend=up_backend).connect(title=up_title)
 app_window = main_window.window(title=up_title)
 time.sleep(3)
 app_window.print_control_identifiers()
pass

def clickevent(up_backend,up_title,upe_title,upe_autoid,upe_controlyype):
 main_window = Application(backend=up_backend).connect(title=up_title)
 app_window = main_window.window(title=up_title)
 time.sleep(3)
 click_event =app_window.child_window(title=upe_title,auto_id=upe_autoid,control_type=upe_controlyype,found_index=0).wrapper_object()
 click_event.click_input()
 pass

def clickevent1(up_backend,up_title,upe_title,upe_autoid,upe_controlyype):
 main_window = Application(backend=up_backend).connect(title=up_title)
 app_window = main_window.window(title=up_title)
 time.sleep(3)
 click_event =app_window.child_window(title=upe_title,auto_id=upe_autoid,control_type=upe_controlyype,found_index=2).wrapper_object()
 click_event.click_input()
 pass


def settextevent(up_backend,up_title,up_text):
 main_window = Application(backend=up_backend).connect(title=up_title)
 app_window = main_window.window(title=up_title)
 time.sleep(3)
 send_keys(up_text,with_spaces=True)
 #main_window.type_keys(up_text)
 #main_window.set_text(up_text)
 #text_sending=main_window.send_keys(up_text).wrapper_object()
 #settext_event =app_window.child_window(auto_id="InputBarTextBox",control_type="text").wrapper_object()
 #settext_event.send_keys(up_text)
 pass
def enterkey():
 send_keys("{ENTER}")
 pass


def setclickevent(up_backend,up_title,upe_title,upe_autoid,upe_controlyype):
 main_window = Application(backend=up_backend).connect(title=up_title)
 app_window = main_window.window(title=up_title)
 time.sleep(3)
 click_event =app_window.child_window(title=upe_title,auto_id=upe_autoid,control_type=upe_controlyype,found_index=0).wrapper_object()
 click_event.invoke()
 pass