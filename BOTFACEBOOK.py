from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import random


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver
def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)

driver = iniciar_driver()
driver.get('https://www.facebook.com/')
sleep(3)
email = driver.find_element(By.XPATH,"//input[@id='email']")
usuario = 'email usuario'
email.click()
sleep(3)
digitar_naturalmente(usuario,email)
sleep(3)
senha = driver.find_element(By.XPATH,"//input[@id='pass']")
usuario_senha = 'senha usuario'
senha.click()
sleep(3)
digitar_naturalmente(usuario_senha,senha)
sleep(3)
entrar = driver.find_element(By.XPATH,"//button[@name='login']")
entrar.click()
sleep(10)
criar_publi = driver.find_element(By.XPATH,"//div[@class='xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe']")
criar_publi.click()
sleep(3)
campo_digitar = driver.find_element(By.XPATH,"//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
texto = 'programador'
digitar_naturalmente(texto,campo_digitar)
sleep(3)
publicar = driver.find_element(By.XPATH,"//div[@class='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67']")
publicar.click()
input()
driver.close