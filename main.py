from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://www.google.com.br/")
    pagina.fill('xpath=//*[@id="APjFqb"]', "Engenheiro de Software")
    pagina.locator('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
    time.sleep(10)