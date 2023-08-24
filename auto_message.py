import pyautogui
import time

def send_Message(message):
    try:
        pyautogui.write(message)
        pyautogui.press('enter')
    except Exception as e:
        print("Hata oluştu:", e)

def main():
    try:
        # It will start functioning 5 seconds after you run the code. You can modify it.
        time.sleep(5)

        message = input("Göndermek istediğiniz mesajı girin: ")
        while True:
            send_Message(message)
            time.sleep(0)  # You can modify the time interval between messages.
    except KeyboardInterrupt:
        print("\nUygulama kullanıcı tarafından durduruldu.")

if __name__ == "__main__":
    main()
