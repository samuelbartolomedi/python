#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Desenvolvido por Samuel Bartolomedi para Camisc
#Abril/2021
#automatização download e instalação spark

import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1
pyautogui.alert("Vai começar, clique OK ou enter e não mexa no pc")

#baixar spark
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://igniterealtime.org/projects/spark/"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.click(73, 467)
time.sleep(1)
pyautogui.click(334, 368)
time.sleep(1)
pyautogui.click(199, 411)

