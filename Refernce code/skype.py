from pywinauto.application import Application
from pywinauto import keyboard
from pywinauto import taskbar
from pywinauto import Desktop
import time

#app = (Application(backend='uia').start('whatsapp.exe').connect(title='WhatsApp', timeout=30))

#time.sleep(5)

#app.Skype.print_control_identifiers()

app_name = 'WhatsApp'
desktop = Desktop(backend="uia")
taskbar = desktop.taskbar  #["Notification chevron button"]

app_icon = taskbar.child_window(title=app_name,control_type="Button")
app_icon.click_input()
time.sleep(3)

main_window = Application(backend='uia').connect(title = "WhatsApp")

time.sleep(3)
main_window.WhatsApp.print_control_identifiers()

#icon = taskbar.app_start(app_name)

#icon.click_input()

