import pyautogui
import time
import webbrowser
import os
from sys import platform


time.sleep(1)

def Shape():
    print ('''

██████╗░███████╗██████╗░██████╗░░█████╗░██████╗░░░░░░██╗██╗    
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗░░░░░██║██║
██║░░██║█████╗░░██████╔╝██████╔╝███████║██║░░██║░░░░░██║██║
██║░░██║██╔══╝░░██╔══██╗██╔══██╗██╔══██║██║░░██║██╗░░██║██║
██████╔╝███████╗██║░░██║██║░░██║██║░░██║██████╔╝╚█████╔╝██║
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝

                                               **  B76F  **

''')
    time.sleep(1.25)

def My_Accounts_Social_Media():
    Following = pyautogui.confirm('Do You Want To Follow ME ? ', buttons =['YES', 'NO'])
    if Following == "YES":
        def Instagram():
            webbrowser.open("https://instagram.com/derradj.i")
        def Github():
            webbrowser.open_new("https://github.com/derradjib76f")
        Instagram()
        time.sleep(1.32)
        Github()
    else:
        print (" -- ENJOY DUDE !! Good_Luck !! --")



def __Bot__():
    time.sleep(1)
    Bot = pyautogui.confirm('Please Choose The Bot :', buttons =['Likes', 'Messages', 'Comments' , 'Login'])
    if platform == "linux" or platform == "linux2":
        os.system("bash Basics_Linux.sh")
        def Excute_Bot_Linux():
            if Bot == "Likes":
                os.system("cd internet Bot/Bot Likes")
                time.sleep(0.1)
                os.system("python3 BOT_Likes.py")
            elif Bot == "Messages":
                os.system("cd internet Bot/Bot Messages")
                time.sleep(0.1)
                os.system("python3 BOT_Messages.py")
            elif Bot == "Comments":
                os.system("cd internet Bot/Bot Comments")
                time.sleep(0.1)
                os.system("python3 BOT_Comments.py")
            elif Bot == "Login":
                os.system("cd internet Bot/__Bot_Login__")
                time.sleep(0.1)
                os.system("python3 __Bot_Login__.py")
            else:
                print ("!!")
                    
        Excute_Bot_Linux()

    elif platform == "win32":
        def Excute_Bot_Windows():
            if Bot == "Likes":
                os.system("start Likes.bat")
            elif Bot == "Messages":
                os.system("start Messages.bat")
            elif Bot == "Comments":
                os.system("start Comments.bat")
            elif Bot == "Login":
                os.system("start Login.bat")
            else:
                print ("!!")

        Excute_Bot_Windows()

    else:
        print ("!!")


def __Main__():
    
    Shape()
    My_Accounts_Social_Media()
    __Bot__()

__Main__()

