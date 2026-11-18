import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

# 1. Abrir o portal da Gupy (https://portal.gupy.io)

# 2. Encontrar o campo de busca, digitar "vagas jr" e apertar ENTER

# 3. Capturar todos os cards de vagas com find_elements()

# 4. Percorrer a lista e exibir os dados e o link de cada vaga
