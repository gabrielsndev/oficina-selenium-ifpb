import time
from selenium import webdriver
import sys 
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from credenciais import USUARIO, SENHA

# 1. Configurações do Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Não fecha o Chrome quando o script acaba
options.add_argument("--start-maximized")        # Abre em tela cheia
options.add_argument("--disable-notifications")  # Bloqueia pop-up nativo do navegador

# 2. Inicializa o driver e o objeto de espera explícita (até 15s)
driver = webdriver.Chrome(options=options)

# 3. Acessa a página inicial
driver.get("https://www.instagram.com/")

campo_email = driver.find_element(By.CSS_SELECTOR, "input[name=email]")
campo_email.send_keys(USUARIO)
campo_senha = driver.find_element(By.CSS_SELECTOR, "input[name=pass]")
campo_senha.send_keys(SENHA)
driver.find_element(By.CSS_SELECTOR, "div[aria-label='Entrar']").click()

# Fazer o 2FA
time.sleep(5)

# Acessando o chat
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(5)
driver.find_element(By.XPATH, "//span[text()='brenno']").click()
#driver.find_element(By.XPATH, "//span[text()='bertlbrn']").click()
print("Acessando o chat...")

# Cobrando meu pix

time.sleep(2)
caixa_msg = driver.find_element(By.CSS_SELECTOR, "div[aria-placeholder='Mensagem...']")
caixa_msg.send_keys("E ai Brenno, beleza? E aquele Pix que voce ta me devendo, sai hoje?")
time.sleep(1)
caixa_msg.send_keys(Keys.ENTER)