from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from utils import login


def test_carrito(driver):
    
    try:
        # Ir al sitio y validar login pero importado desde utils.py
        login(driver)
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

        # Busca productos
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0, "No se encontraron productos en el catálogo"
        print(f"Se encontraron {len(productos)} productos")

        
        productos[0].find_element(By.TAG_NAME, 'button').click()
        
        # Confirmar que el badge del carrito muestra 1
        badge = driver.find_element(By.CLASS_NAME,
        'shopping_cart_badge').text
        assert badge == '1'
        os.makedirs("prints", exist_ok=True)
        screenshot_path = os.path.join("prints", "producto_en_carrito.png")
        driver.save_screenshot(screenshot_path)
        print('Carrito OK →', badge)

    except Exception as e:
        print(f"Error en test login: {e}")
        raise