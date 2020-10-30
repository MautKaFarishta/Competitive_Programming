import pyautogui,time
time.sleep(5)
f = open("Practice/bee",'r')
for word in f:
   pyautogui.typewrite(word)
   pyautogui.press("enter")
   
   
   
     
     