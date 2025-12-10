from pages.inventory_page import InventoryPage
from utils.logger import logger
import pytest
import os

def test_checkout_completo(login_in_driver):
    driver = login_in_driver
    inventory = InventoryPage(driver)
    
    logger.info("Iniciando test de checkout completo")
    
    # 1. Agregar producto
    inventory.agregar_primer_producto()
    
    # 2. Ir al carrito
    cart_page = inventory.ir_al_carrito()
    
    # 3. Proceder al checkout
    cart_page.proceder_checkout()
    
    # 4. Completar info 
    from pages.checkout_page import CheckoutPage
    checkout = CheckoutPage(driver)
    
    logger.info("Completando información de envío")
    checkout.completar_informacion_envio("Brenda", "Wugner", "1234")
    
    # 5. Finalizar compra (Checkout Step 2)
    checkout.finalizar_compra()
    
    # 6. Validar mensaje final
    mensaje = checkout.obtener_mensaje_confirmacion()
    logger.info(f"Mensaje obtenido: {mensaje}")
    assert "Thank you for your order" in mensaje or "THANK YOU FOR YOUR ORDER" in mensaje
    
    # Screenshot final
    os.makedirs("reports/screenshots", exist_ok=True)
    driver.save_screenshot("reports/screenshots/checkout_completed.png")
