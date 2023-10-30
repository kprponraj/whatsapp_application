from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import keyboard
from base import *
import TC001DP

"""

def test_sendingtextfromlist():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Ishu','Title','Text')
 settextevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}',f'{TC001DP.up_text}')
 enterkey()
 printidentifiers(f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
pass
 
"""

"""

def test_sendingtextfromnewchatlist():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Create new conversation','NewConvoButton','Button')
 settextevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}',f'{TC001DP.up_contactpersonname}')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Arun Impiger','Title','Text')
 settextevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}',f'{TC001DP.up_msgforarun}')
 #enterkey()
 printidentifiers(f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
pass

"""



"""
def test_UploadingProfilePicture():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}', f'{TC001DP.up_title}')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Profile','ProfileNavigationItem','ListItem')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Profile image','','Button')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','TestData (pinned)','','TreeItem')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','File name:','1148','Edit')
 settextevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}',f'{TC001DP.up_profilepicname}')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Open','1','Button')

#printidentifiers(f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
pass
"""
"""

def test_RemovingProfileicon():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}', f'{TC001DP.up_title}')
 #clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Maximize WhatsApp','Maximize','Button')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Profile','ProfileNavigationItem','ListItem')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Profile image','','Button')
#printidentifiers(f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
 setclickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Remove image','','MenuItem')
pass

"""
"""
def test_callingtheuser():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}', f'{TC001DP.up_title}')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Calls', 'CallsNavigationItem', 'ListItem')
 #printidentifiers(f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
 #clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Ishu', 'Title', 'Text')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Create new conversation', 'NewCallButton', 'Button')
 settextevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', f'{TC001DP.up_audiocallname}')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Ishu', 'Title', 'Text')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', '', 'AudioCallButton', 'Button')
 printidentifiers(f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
pass
"""

"""
def test_creatingGroup():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Create new conversation','NewConvoButton','Button')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','New group','CreateGroupButton','Button')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Ishu','Title','Text')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Next','NextButton','Button')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Provide a group name','','Text')
#printidentifiers(f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
 settextevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}',f'{TC001DP.up_groupname}')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Disappearing messages','EphemeralMessagesExpiration','ComboBox')
#printidentifiers(f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}',f'{TC001DP.up_dpmsg}','','Text')
 clickevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}','Create','NextButton','Button')
#printidentifiers(f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
pass

"""
"""
def test_AddingNewMemberInGroup():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}', f'{TC001DP.up_title}')
 settextevent(f'{TC001DP.up_backend}',f'{TC001DP.up_title}',f'{TC001DP.up_groupname}')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Automation Group', 'Title', 'Text')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Automation Group', '', 'Text')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Participants', 'ParticipantsButton', 'ListItem')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Add participants', '', 'Button')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Saran', 'Title', 'Text')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Add 1 person', 'AddParticipantButton', 'Button')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Yes', '', 'Button')

 printidentifiers(f'{TC001DP.up_backend}',f'{TC001DP.up_title}')
pass
"""
"""
def test_HandlingToggleButton():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}', f'{TC001DP.up_title}')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Open Settings', 'SettingNavigationItem', 'ListItem')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Notifications', 'NotificationsButton', 'ListItem')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Text preview', 'ShowContentMessagesNotificationSwitch', 'Button')

pass
"""
"""
def test_ChangingTheTheme():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}', f'{TC001DP.up_title}')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Open Settings', 'SettingNavigationItem', 'ListItem')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Personalization', 'PersonalizeButton', 'ListItem')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'App theme selector', 'ThemeCombobox', 'ComboBox')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Light', '', 'Text')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'OK', '', 'Text')
pass
"""

"""
def test_ApplyingFliters():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}', f'{TC001DP.up_title}')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Filter chats by', 'FilterButton', 'Button')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Contacts', 'TextBlock', 'Text')
pass
"""
"""
def test_updatingaboutandstatus():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}', f'{TC001DP.up_title}')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Profile', 'ProfileNavigationItem', 'ListItem')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Name, Start editing', 'EditButton', 'Button')
 clearkey()
 settextevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Ponraj')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'About, Start editing', 'EditButton', 'Button')
 clearkey()
 settextevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Status')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Name, Start editing', 'EditButton', 'Button')

 printidentifiers(f'{TC001DP.up_backend}', f'{TC001DP.up_title}')
pass
"""
"""
def test_reactingmessage():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}', f'{TC001DP.up_title}')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Ishu', 'Title', 'Text')
 #clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'testing\r\n', 'TextBlock', 'Text')
 clickevent3(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', '', 'EmojiIcon', 'Text')
 clickevent3(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', '', 'EmojiIcon', 'Text')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', '❤️', '', 'ListItem')
 #child_window(title="Copy", control_type="Button")
pass
"""

"""
def test_deletemessagefromchat():
 launchingtheapplicationfromtaskbar(f'{TC001DP.up_name}', f'{TC001DP.up_backend}', f'{TC001DP.up_title}')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Ishu', 'Title', 'Text')
 #clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'testing\r\n', 'TextBlock', 'Text')
 clickevent3(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', '', 'EmojiIcon', 'Text')
 clickevent3(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', '', 'EmojiIcon', 'Text')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Delete', '', 'Button')
 clickevent(f'{TC001DP.up_backend}', f'{TC001DP.up_title}', 'Delete for me', '', 'Button')
 #printidentifiers(f'{TC001DP.up_backend}', f'{TC001DP.up_title}')
pass
"""

