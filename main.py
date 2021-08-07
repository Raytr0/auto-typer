import time
import pyautogui
import keyboard

while True:
    if keyboard.is_pressed('shift'):
        text = open("outputtext.txt")
        for each_line in text:
            pyautogui.typewrite(each_line)