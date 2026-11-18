import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from credenciais import USUARIO, SENHA

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

# 1. Abre o Instagram e faz login
driver.get("https://www.instagram.com/")

# TODO: Preencher email, senha e clicar em Entrar

# 2. Pausa para verificação em 2 etapas (2FA)
time.sleep(20)

# 3. Ir direto para a caixa de entrada do Direct
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(5)

# TODO: Clicar no amigo pelo XPath (//span[text()='...'])

# TODO: Encontrar a caixa de texto (div[aria-placeholder='Mensagem...']) e enviar a mensagem com Keys.ENTER
