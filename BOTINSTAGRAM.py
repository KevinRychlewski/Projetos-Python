import pyautogui
import webbrowser
from time import sleep
# Entrar no instagram
webbrowser.open('https://www.instagram.com/')
# Clicar pra escrever email
pyautogui.click(1062,351,duration=2)
pyautogui.typewrite('usuário')
# Clicar para escrever a senha
pyautogui.click(1057,393,duration=2)
pyautogui.typewrite('senha usuário')
# Clicar em login
pyautogui.click(1144,445,duration=2)
sleep(2)
# Clicar para nao salvar as informacoes
pyautogui.click(1115,613,duration=2)
sleep(5)
# Clicar em pesquisar
pyautogui.click(77,280,duration=2)
sleep(1)
# Digitar nome do perfil
pyautogui.typewrite('dreams')
# Clicar no perfil
pyautogui.click(197,251,duration=2)
sleep(2)
# Descer o feed um pouco
pyautogui.scroll(-600)
# Clicar no ultimo video
pyautogui.click(770,618,duration=2)
sleep(3)
# Curtir
pyautogui.click(981,886,duration=2)
# Comentar
pyautogui.click(1093,991,duration=2)
pyautogui.click(981,996,duration=2)
pyautogui.doubleClick(1227,693,duration=2)
pyautogui.click(1415,992,duration=2)