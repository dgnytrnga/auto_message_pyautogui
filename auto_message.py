import pyautogui
import time

time.sleep(10)

#Edit the message to be written in the pyautogui.message('') section yourself.
def mesaj():
    pyautogui.write("Message")
    pyautogui.press('enter')

while True:
    mesaj()
    time.sleep(0)
