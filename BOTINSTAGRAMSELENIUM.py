from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.support import expected_conditions as condicao_esperada

# Iniciar o webdriver


def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=en-US', '--window-size=1920,1080',
                 '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1

    })

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait


driver, wait = iniciar_driver()
# entrar no instagram
driver.get('https://www.instagram.com/')
# achar e clicar pra escrever o usuario
usuario = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))
usuario.click()
usuario.send_keys('Usuário')
sleep(2)
# achar e clicar para escrever a senha
senha = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')))
senha.click()
senha.send_keys('Senha usuário')
sleep(2)
# clicar em entrar
entrar = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH,'//*[@id="loginForm"]/div/div[3]')))
entrar.click()
sleep(2)
# Entrar na conta q quiser
driver.get('https://www.instagram.com/dreamsaudiovisual/')
# Clicar na postagem
clicar_postagem = wait.until(condicao_esperada.visibility_of_any_elements_located(
    (By.XPATH,"//div[@class='_aagu']")))
clicar_postagem[0].click()
# Verificar se foi curtido ou nao
try:
        verifica_curtida = driver.find_element(By.XPATH,
                                               '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]//div[@role="button"]//*[@aria-label="Curtir"]')
except:
    print('A imagem já havia sido curtida.')
else:
    botao_curtir = driver.find_elements(By.XPATH,
                                            '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]//div[@role="button"]')
    sleep(5)
    driver.execute_script('arguments[0].click()', botao_curtir[0])
    print('a imagem foi curtida')


input('')
driver.close()