import pyautogui
import time

#It will start functioning 5 seconds after you run the code. You can modify it.
time.sleep(5)

#Edit the message to be written in the pyautogui.message('') section yourself.
def send_Message():
    pyautogui.write("Message")
    pyautogui.press('enter')

while True:
    send_Message()
    time.sleep(0)
    #You can modify the (time.sleep()) part to change the time intervals of message delivery.
