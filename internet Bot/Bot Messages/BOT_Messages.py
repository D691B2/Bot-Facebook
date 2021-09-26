import pyautogui
import webbrowser
import time

def OpenBrowser(): # Open Browser and site Facebook #
    webbrowser.open("https://www.facebook.com")
    time.sleep(32.5)


def Search_ON_Friends(): # Search on Friends and Open Conversation
    time.sleep(5.23)
    Search_Friend = pyautogui.locateCenterOnScreen("IMG/Search.PNG")
    time.sleep(0.75)
    pyautogui.click(Search_Friend)
    time.sleep(1.25)
    __Name__ = str(pyautogui.prompt('Enter The Name OF Your Friend : '))
    pyautogui.typewrite(__Name__, interval=0.15)
    time.sleep(0.865)
    pyautogui.press('down', presses=1)
    time.sleep(0.35)
    pyautogui.press('enter')
    time.sleep(7.88)
    Message_Friend = pyautogui.locateCenterOnScreen("IMG/Message.png")
    time.sleep(1.5)
    pyautogui.click(Message_Friend)
    time.sleep(1.23)



def StartMessages(): # Start Send Messages #
    __Message__ = str (pyautogui.prompt('Write Your Message Here : '))
    __Number_Messages__ = int (pyautogui.prompt('Number OF Messages Here : '))
    for Message in range(__Number_Messages__):
        pyautogui.typewrite(__Message__)
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.74)


def ___Main___():
    OpenBrowser()
    time.sleep(0.22)
    Search_ON_Friends()
    time.sleep(1.22)
    StartMessages()

___Main___()
