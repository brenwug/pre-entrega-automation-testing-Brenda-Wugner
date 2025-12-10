from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import os

def test_carrito(login_in_driver):
    driver = login_in_driver
    inventory_page = InventoryPage(driver)
    
    # Obtener datos del producto y añadirlo al carrito
    datos_producto = inventory_page.obtener_datos_primer_producto()
    nombre_producto_agregado = datos_producto["nombre"]
    inventory_page.agregar_primer_producto()
    
    # Verificar que el badge del carrito muestra 1
    assert inventory_page.obtener_contador_carrito() == 1
    print(f"Producto agregado. Badge muestra: {inventory_page.obtener_contador_carrito()}")

    os.makedirs("reports/screenshots", exist_ok=True)
    screenshot_path = os.path.join("reports/screenshots", "producto_en_carrito.png")
    driver.save_screenshot(screenshot_path)
    
    # Navegar al carrito de compras
    cart_page = inventory_page.ir_al_carrito()
    
    # Validar que se haya agregado el producto correcto en el carrito
    nombres_en_carrito = cart_page.obtener_nombres_productos()
    assert nombre_producto_agregado in nombres_en_carrito, "El producto añadido no se agregó correctamente"
    print(f"Producto verificado en carrito: {nombre_producto_agregado}")

