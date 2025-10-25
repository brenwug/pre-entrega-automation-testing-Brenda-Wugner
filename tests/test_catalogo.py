
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from utils import login

def test_catalogo(driver):
    
    try:
        # Ir al sitio y validar login pero importado desde utils.py
        login(driver)
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

 # Validar que el título en inventory sea Products
        titulo = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "title"))
        ).text
        assert titulo == "Products", f"El título esperado era Products pero se obtuvo '{titulo}'"
        print(f"El título en la página es '{titulo}'")


        # Validar que haya al menos un producto visible

        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0, "No se encontraron productos en el catálogo"
        print(f"Se encontraron {len(productos)} productos")

        # Obtener nombre y precio del primer producto
        primer_producto = productos[0]
        nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"Primer producto: {nombre} - {precio}")

        os.makedirs("prints", exist_ok=True)
        screenshot_path = os.path.join("prints", "catalogo.png")
        driver.save_screenshot(screenshot_path)

        # Validar menu
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed(), "El menú no está visible"
        print("El menú está disponible")

        #validar filtro
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed(), "El filtro no está visible"
        print("El filtro está ok")

        # Validar carrito
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        assert carrito.is_displayed(), "El carrito no se encuentra"
        print("Está el carrito")

    except Exception as e:
        print(f"Error en test catalogo: {e}")
        raise
