"""--> Take a number from the user and draw a pyramid using PyAutoGUI

5
#
##
###
####
#####

1
#

--------------------------------------------------------------------"""

import pyautogui
import time

N = int(input())

time.sleep(2)  # --> Sleep for 2 sec

pyautogui.press("enter")  # --> Etau kaj kore + Nicer tau kaj kore...
# for _ in range(4):  # --> Random 4 time selected
#     pyautogui.press("backspace")

# for i in range(1, N + 1):
#     pyautogui.typewrite("#" * i, interval=0.05)
#     pyautogui.press("enter")

for i in range(1, N + 1):
    pyautogui.typewrite("🖕🏻", interval=0.05)
    pyautogui.press("enter")
