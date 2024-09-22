import time
import pyautogui
import keyboard
import pyperclip

keyboard.wait("ctrl+alt+i")
time.sleep(1)

text = pyperclip.paste()

pyautogui.press("backspace")
pyautogui.write(text ,0.01)