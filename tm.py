import pyautogui
import morse_talk as mtalk

txt = "code"

mcode = mtalk.encode(txt, encoding_type='binary')
print(mcode)

txt = list(txt)
print(txt)


# pyautogui.press('f1')