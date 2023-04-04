# Esse programa faz com que o cursor do seu mouse mova-se sozinho através de coordenadas.

import pyautogui

print("Presione CTRL-C para sair.")

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'Histórico de Cordenadas - X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + "\n"
        pyautogui.moveTo(398, 54, duration=0.7)
        pyautogui.moveTo(280, 53, duration=0.7)
        pyautogui.moveTo(500, 54, duration=0.7)
        pyautogui.moveTo(58, 53, duration=0.7)
        pyautogui.click(1263, 404, button="left")
        print(positionStr, end="")
except KeyboardInterrupt:
    print('\b' * len(positionStr), end='', flush=True)