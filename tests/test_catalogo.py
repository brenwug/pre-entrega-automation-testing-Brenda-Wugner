
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.datos import leer_json_productos
from pages.inventory_page import InventoryPage
import os

def test_catalogo(login_in_driver):
    driver = login_in_driver
    inventory = InventoryPage(driver)
    
    try:
        # Validar que el título en inventory sea Products
        titulo = inventory.obtener_titulo()
        assert titulo == "Products", f"El título esperado era Products pero se obtuvo '{titulo}'"
        print(f"El título en la página es '{titulo}'")


        # Validar que haya al menos un producto visible
        productos = inventory.obtener_productos()
        assert len(productos) > 0, "No se encontraron productos en el catálogo"
        print(f"Se encontraron {len(productos)} productos")

        # Obtener nombre y precio del primer producto
        prod_data = inventory.obtener_datos_primer_producto()
        print(f"Primer producto: {prod_data['nombre']} - {prod_data['precio']}")

        os.makedirs("reports", exist_ok=True)
        screenshot_path = os.path.join("reports", "catalogo.png")
        driver.save_screenshot(screenshot_path)

        # Validar menu
        assert inventory.es_menu_visible(), "El menú no está visible"
        print("El menú está disponible")

        #validar filtro
        assert inventory.es_filtro_visible(), "El filtro no está visible"
        print("El filtro está ok")

        # Validar carrito
        assert inventory.es_carrito_visible(), "El carrito no se encuentra"
        print("Está el carrito")

    except Exception as e:
        print(f"Error en test catalogo: {e}")
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