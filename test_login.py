from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login():
   
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Ir al sitio
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)

        # Completar login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)

        # Validar resultado
        assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario"
        driver.save_screenshot("login_exitoso.png")
        print("Login exitoso y validado correctamente")

    except Exception as e:
        print(f"Error en test login: {e}")
        raise

    finally:
        driver.quit()