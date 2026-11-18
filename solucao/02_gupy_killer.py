import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Configurações do Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

# 2. Inicializa o driver
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

# 3. Abre a página inicial da Gupy
driver.get("https://portal.gupy.io/")


# 4. Procurando por vagas:

campo_busca = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Busque por uma vaga']")
campo_busca.send_keys("vagas jr" + Keys.ENTER)

time.sleep(3)  # Dá tempo dos cards renderizarem na tela

# 5. Pega TODOS os cards de vagas da página (find_elements no plural!)
vagas = driver.find_elements(By.CSS_SELECTOR, "a[href*='/job/']")
print(f"🔎 Encontrei {len(vagas)} vagas na tela!\n")

for vaga in vagas:
    # 6. Pega o título da vaga
    titulo = vaga.find_element(By.CSS_SELECTOR, "h3").text
    # 7. Pega a empresa da vaga
    empresa = vaga.find_element(By.CSS_SELECTOR, "p").text
    # 8. Pega o link da vaga
    link = vaga.get_attribute("href")
    print(f"📌 {titulo} - {empresa} - {link}")