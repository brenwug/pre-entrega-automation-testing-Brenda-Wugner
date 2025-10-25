from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

def test_login():
   
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Ir al sitio
        driver.get("https://www.saucedemo.com/")

        # Validar login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

        # Validar resultado /inventory.html
        assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario"
        driver.save_screenshot("login_exitoso.png")
        print("Login exitoso y validado correctamente")

        titulo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        ).text
        assert titulo == "Products", f"El título esperado era Products pero se obtuvo '{titulo}"
        print(f"El título en la página es '{titulo}'")

    except Exception as e:
        print(f"Error en test login: {e}")
        raise

    finally:
        driver.quit()