import os
import sys 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from credenciais import USUARIO, SENHA

# 1. Configurações do Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")        # Abre em tela cheia
options.add_argument("--disable-notifications")  # Bloqueia pop-up nativo do navegador

# 2. Inicializa o driver

# 3. Acessa a página inicial



# Fazer o 2FA
time.sleep(5)

# Acessando o chat




# Cobrando meu pix


