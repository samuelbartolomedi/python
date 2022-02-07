#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Desenvolvido por Samuel Bartolomedi para Camisc
#Abril/2021
#automatização download e instalação doors

import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1
pyautogui.alert("Vai começar, clique OK ou pressione enter e não mexa no pc")

#instalar doors
time.sleep(2)
pyautogui.press("winleft")
pyautogui.write("Doors.application")
pyautogui.press("up")
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("left")
pyautogui.press("enter")


# In[ ]:




