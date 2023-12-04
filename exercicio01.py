# Criar uma automação com pyautogui pela qual o programa abre o bloco de notas, digita uma mensagem e a salve
import pyautogui
import time

pyautogui.press('winleft') #Apertar no Win
time.sleep(2)
programa = "Bloco de Notas" #Abrir Bloco de notas
time.sleep(2)
pyautogui.write(programa) 
time.sleep(2)
pyautogui.press('enter')

time.sleep(2)

frase = 'Programado do Bradesco'
pyautogui.write(frase)

time.sleep(2)
pyautogui.hotkey('Ctrl', 'S')
time.sleep(1)
pyautogui.write('Programado.txt')
time.sleep(1)
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')


