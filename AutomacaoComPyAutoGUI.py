import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.alert("O nosso algoritmo vai rodar, pressiona OK, para começar!")

# faça um screenshot e abre o paint
pyautogui.press('printscreen')
pyautogui.press('winleft')
pyautogui.write('paint')
pyautogui.press('enter')
time.sleep(1)

# dê clique e cole a imagen
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# salve a imagen e feche o programa
pyautogui.hotkey('alt','f4')
time.sleep(1)
pyautogui.press('enter')
pyautogui.write('screen')
pyautogui.press('enter')
time.sleep(1)

# avise ao terminar as tarefas
pyautogui.alert("Acabamos de executar o nosso algoritmo, pressione OK, para terminar.")

#criado por JOSE EURICO
