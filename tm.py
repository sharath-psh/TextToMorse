import pyautogui
import morse_talk as mtalk

mcode = mtalk.encode('Sharath', encoding_type='binary')
print(mcode)



# Python3 program to Split string into characters 
def split(word): 
	return [char for char in word] 
	
# Driver code 
word = 'geeks'
print(split(word)) 


# pyautogui.press('f1')