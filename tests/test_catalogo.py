
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.datos import leer_json_productos
from pages.inventory_page import InventoryPage
from utils.logger import logger
import os

def test_catalogo(login_in_driver):
    driver = login_in_driver
    inventory = InventoryPage(driver)
    
    try:
        # Validar que el título en inventory sea Products
        titulo = inventory.obtener_titulo()
        assert titulo == "Products", f"El título esperado era Products pero se obtuvo '{titulo}'"
        logger.info(f"El título en la página es '{titulo}'")


        # Validar que haya al menos un producto visible
        productos = inventory.obtener_productos()
        assert len(productos) > 0, "No se encontraron productos en el catálogo"
        logger.info(f"Se encontraron {len(productos)} productos")

        # Obtener nombre y precio del primer producto
        prod_data = inventory.obtener_datos_primer_producto()
        logger.info(f"Primer producto: {prod_data['nombre']} - {prod_data['precio']}")

        os.makedirs("reports", exist_ok=True)
        screenshot_path = os.path.join("reports", "catalogo.png")
        driver.save_screenshot(screenshot_path)

        # Validar menu
        assert inventory.es_menu_visible(), "El menú no está visible"
        logger.info("El menú está disponible")

        #validar filtro
        assert inventory.es_filtro_visible(), "El filtro no está visible"
        logger.info("El filtro está ok")

        # Validar carrito
        assert inventory.es_carrito_visible(), "El carrito no se encuentra"
        logger.info("El carrito está visible")

    except Exception as e:
        logger.error(f"Error en test catalogo: {e}")
        raise

def test_productos_existentes_en_catalogo(login_in_driver):
    driver = login_in_driver
    inventory = InventoryPage(driver)

    WebDriverWait(driver,10).until(EC.url_contains("/inventory.html"))

    nombres_pagina = inventory.obtener_nombres_productos()

    nombres_json = leer_json_productos("datos/productos.json")

    logger.info(f"Productos esperados del Json: {nombres_json}")
    logger.info(f"Productos encontrados en página: {nombres_pagina}")

    for nombre_esperado in nombres_json:
        assert nombre_esperado in nombres_pagina, \
        f"El producto '{nombre_esperado}' no aparece en el catálogo de la página"

    logger.info("Todos los productos del JSON están en el catálogo")