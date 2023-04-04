# Nesse programa irei fazer com que o mouse "digital" se mova sozinho e consiga desenhar um quadrado!!

import pyautogui, time

time.sleep(2)
pyautogui.click(365, 750, button="left")
pyautogui.moveTo(605, 183)
distance = 200


while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2)

# print(pyautogui.position())