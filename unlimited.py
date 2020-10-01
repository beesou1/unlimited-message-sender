import pyautogui
import time
 

f = input("write your message:")

for word in f:
     while True:
          time.sleep(2)
          pyautogui.typewrite(f)
          time.sleep(1)
          pyautogui.press("enter")

