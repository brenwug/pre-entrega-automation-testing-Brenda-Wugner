
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from pages.login_page import LoginPage

def test_login(driver):

    login_page = LoginPage(driver)
    login_page.abrir_pagina().login_completo("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

        # Validar resultado /inventory.html
    assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario"

    os.makedirs("reports", exist_ok=True)
    screenshot_path = os.path.join("reports", "login_exitoso.png")
    driver.save_screenshot(screenshot_path)
    print("Login exitoso y validado correctamente")
