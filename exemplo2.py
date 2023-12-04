import pyautogui
import time

# Abrir o paint

pyautogui.press('winleft')
programa = "Paint"
pyautogui.write(programa)
pyautogui.press('enter')

# Aguarda a abertura do programa
time.sleep(2)

# Mover cursor para área de desenho

x = 11
y = 1057


pyautogui.moveTo(x, y)

#Criar um desenho simples

pyautogui.dragTo(600,600, duration=1, button='left') # Desenha uma linha simples 

pyautogui.dragTo(300,300, duration=1, button='left')# Desenha uma linha simples 



