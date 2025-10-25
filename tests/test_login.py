
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from utils import login


def test_login(driver):


    try:
        # Ir al sitio y validar login pero importado desde utils.py
        login(driver)

        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

        # Validar resultado /inventory.html
        assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario"
        os.makedirs("prints", exist_ok=True)
        screenshot_path = os.path.join("prints", "login_exitoso.png")
        driver.save_screenshot(screenshot_path)
        print("Login exitoso y validado correctamente")

    except Exception as e:
        print(f"Error en test login: {e}")
        raise

