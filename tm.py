import pyautogui
import morse_talk as mtalk

mcode = mtalk.encode('Sharath', encoding_type='binary')
print(mcode)

pyautogui.press('f1')