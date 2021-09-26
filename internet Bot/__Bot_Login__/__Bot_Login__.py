import pyautogui
import time


def Login(): #  this function to login in your facebook account  #
    time.sleep(1)
    email = pyautogui.locateCenterOnScreen("IMG/email_login.PNG")
    time.sleep(1.88)
    pyautogui.click(email)
    time.sleep(0.52)
    number_phone_or_id = pyautogui.prompt(text='Put Your Number Phone OR ID Please', title='Number_Phone_OR_ID' , default='DerradjiB76F')
    pyautogui.typewrite(number_phone_or_id)
    time.sleep(1.52)
    #pyaitogui.moveTo(1290 , 35)
    #pyautogui.click()
    password = pyautogui.locateCenterOnScreen("IMG/password_login.PNG")
    time.sleep(1.88)
    pyautogui.click(password)
    time.sleep(0.25)
    Password_Account = pyautogui.password(text='Please Enter Your Password', title='Password Account', default='', mask='#')
    pyautogui.typewrite(Password_Account)
    time.sleep(1.895)
    login = pyautogui.locateCenterOnScreen("IMG/login_button.PNG")
    time.sleep(1.88)
    pyautogui.click(login)
    time.sleep(30.58)

Login()
