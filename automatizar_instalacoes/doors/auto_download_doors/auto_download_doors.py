#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Desenvolvido por Samuel Bartolomedi para Camisc
#Abril/2021
#automatização download e instalação doors

import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1
pyautogui.alert("Vai começar, clique OK ou pressione enter e não mexa no pc")

#baixar doors
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
link = "http://ws.camisc.coop.br/doors/Doors.application"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(2)
#pyautogui.click(394, 531)
pyautogui.alert("Verifique sua pasta de downloads :)")

