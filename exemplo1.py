# MetaTrader
# ProftPro

# Automação de interface Desktop

import pyautogui
import time

# time.sleep(5)  # Aguardar alguns segundos antes de iniciar

# # largura, altura = pyautogui.size()  # Obtenha e imprima as dimensões da tela
# # print(f"A largura da tela é: {largura}\n. A altura da tela: {altura}.")

# # pyautogui.move(200, 200, duration = 2)  # Mover o mouse para as coordenadas (x,y) e clique 
# # pyautogui.click()

# #pyautogui.typewrite("Hello world!")  #Digite algo usando o teclado virtual

while True:
     a, b = pyautogui.position()  #Obter e imprimir a posição atual do mouse
     print(f"A posição atual do mouse é {a} and {b}.")

  #pyautogui("Este é um alerta!")




