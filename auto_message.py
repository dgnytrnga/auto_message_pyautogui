import pyautogui
import time

time.sleep(10)

def mesaj():
    pyautogui.write("Bebecim")
    pyautogui.press('enter')

while True:
    mesaj()
    time.sleep(0)
