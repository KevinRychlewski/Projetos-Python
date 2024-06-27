# CÓDIGO PARA ENVIAR MENSAGEM PRO CONTATO - https://api.whatsapp.com/send?phone=(numero do cll)
import webbrowser
import pyautogui
from time import sleep

telefones = [5511963898128]

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click('coordenada do whatsapp web')
    sleep(10)
    pyautogui.typewrite('mensagem que vc quiser')
    sleep(5)
    pyautogui.press('enter''para enviar')
    sleep(300)

