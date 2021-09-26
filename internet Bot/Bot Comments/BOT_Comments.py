#Python3
#        instagram : https://www.instagram.com/derradj.i
#        github    : https://www.github.com/derradjib76f

#        pip install pyautogui        #
#        pip install time             #
#        pip install webbrowser       #

#  Librarys  #
import pyautogui
import time
import webbrowser

###    CODE    ###


def OpenBrowser(): #  this function to open site www.facebook.com on browser  #
    webbrowser.open("www.facebook.com")
    time.sleep(13.5)


def OpenGroups(): #  this function to open your groups  #
    
    time.sleep(2.5)
    groups = pyautogui.locateCenterOnScreen("IMG/groups_facebook.PNG")
    time.sleep(1.88)
    pyautogui.click(groups)
    time.sleep(4.89)
    
    #  method number two to open groups  #
    #  import os  #
    #  os.system(start browser.exe https://www.facebook.com/groups)  #



def StartComments(): #  this function to starting comments without stoping  #
    
    for Comment in range(1):
        time.sleep(1)
        pyautogui.press('down', presses=10)
        time.sleep(4.5)
        comment = pyautogui.locateCenterOnScreen("IMG/add_comment.PNG")
        time.sleep(2)
        pyautogui.click(comment)
        time.sleep(0.5)
        pyautogui.typewrite("your Comment ...")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.moveTo(244 , 118)
        pyautogui.click()
        time.sleep(1)
        
        num = 1
        num = num + 1
        print ("Done Comment !! : " , num)



def Main(): #  function main to execution other functions in the order  #
    
    OpenBrowser()
    time.sleep(1.5)
    OpenGroups()
    
    while True:
        StartComments()


Main() #  EXECUTE  #
