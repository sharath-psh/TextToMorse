import pyautogui
import morse_talk as mtalk

# print(pyautogui.KEYBOARD_KEYS)

pyautogui.keyDown('fn')
pyautogui.press('f1')

mcode = mtalk.encode('Sharath', encoding_type='binary')
print(mcode)