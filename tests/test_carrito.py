from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.datos import leer_json_productos
import os

def test_carrito(login_in_driver):
    driver = login_in_driver

    try:
        
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

        # Busca productos
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0, "No se encontraron productos en el catálogo"
        print(f"Se encontraron {len(productos)} productos")

        nombre_producto_agregado = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        productos[0].find_element(By.TAG_NAME, 'button').click()
        
        # Confirmar que el badge del carrito muestra 1
        badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
        'shopping_cart_badge'))
        ).text

        assert badge == '1'

        os.makedirs("reports", exist_ok=True)
        screenshot_path = os.path.join("reports", "producto_en_carrito.png")
        driver.save_screenshot(screenshot_path)
        print('Carrito OK =', badge)

        # Navegar al carrito de compras
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Espera hasta que cargue la página del carrito
        WebDriverWait(driver, 10).until(EC.url_contains ("/cart.html"))

        # Obtener el nombre del primer producto en el carrito
        producto_carrito = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
        

        #Validar que se haya agregado el producto correcto en el carrito
        assert producto_carrito == nombre_producto_agregado, "El producto añadido no se agregó"
        print(f"Producto agregado correctamente: {producto_carrito}")


    except Exception as e:
        print(f"Error en test login: {e}")
        raise

def test_productos_existentes_en_catalogo(login_in_driver):
    driver = login_in_driver

    WebDriverWait(driver,10).until(EC.url_contains("/inventory.html"))

    elementos = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    nombres_pagina = [elemento.text for elemento in elementos]

    nombres_json = leer_json_productos("datos/productos.json")

    print("Productos esperados del Json:", nombres_json)
    print("Productos encontrados en página:", nombres_pagina)

    for nombre_esperado in nombres_json:
        assert nombre_esperado in nombres_pagina, \
        f"El producto '{nombre_esperado}' no aparece en el catálogo de la página"

    print("Todos los productos del JSON están en el catálogo")