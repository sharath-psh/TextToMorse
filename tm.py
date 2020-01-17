import pyautogui
import morse_talk as mtalk

#word to convert
txt = input("Enter your text:")
#converts txt to morse code as binary string
mcode = mtalk.encode(txt, encoding_type='binary')
print(mcode)

#typecasts string to list
mcode = list(mcode)
print(mcode)

mcode_lnth = len(mcode)

for i in range(mcode_lnth):  # Use `xrange` for python 2.
    if "1" in mcode[i]:
        pyautogui.press('capslock')
        print("pressing 1")
    elif "0" in mcode[i]:
        pyautogui.press('capslock')
        print("pressing 0")

pyautogui.press('capslock')


print("loop done")