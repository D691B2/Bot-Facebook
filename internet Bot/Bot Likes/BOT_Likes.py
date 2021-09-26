# Python3 #
# pip install pyautogui  #
# pip install webbrowser #
# pip install time       #

#   Librarys   #
import pyautogui
import time
import webbrowser


time.sleep(3)


def OpenBrowser(): # open browser and login to facebook webdite #
    webbrowser.open("https://www.facebook.com")
    time.sleep(32.5)


def Start_Likes(): # Start Likes #
    
    while True:
        pyautogui.press('down', presses=10)
        time.sleep(2)
        _Button_ = pyautogui.locateCenterOnScreen("IMG/like.PNG")
        pyautogui.click(_Button_ , clicks=1)
        time.sleep(0.89)
        pyautogui.moveTo(989, 300)


def __Main__(): # function of execute #
    OpenBrowser()
    Start_Likes()


__Main__() # EXRCUTE #

