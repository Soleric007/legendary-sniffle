import pyautogui
word = 'Hello my name is Solomon, with the help of a python program ive been able to move around without touching my mouse and keyboard. Thank you'
pyautogui.moveTo(1950, 1050, 1)
pyautogui.click()
pyautogui.moveTo(150, 1050, 1)
pyautogui.click()
pyautogui.write('Microsoft Word', interval=0.20)
pyautogui.moveTo(150, 200, 1)
pyautogui.click()
pyautogui.moveTo(300, 300, 3)
pyautogui.click()
pyautogui.moveTo(500, 500, 1)
pyautogui.click()
pyautogui.write(word, interval=0.05)
pyautogui.moveTo(1950, 6, 1)
pyautogui.click()
pyautogui.moveTo(1100, 700, 1)
pyautogui.click()
