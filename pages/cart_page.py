from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) #Verificar que estamos en la página correcta
        self.wait.until(EC.url_contains("cart.html"))

    def obtener_productos_en_carrito(self): #obtiene la lista de productos en el carrito
        return self.driver.find_elements(*self._CART_ITEMS)
    
    def obtener_nombres_productos(self):
        elementos_nombre = self.driver.find_elements(*self._ITEM_NAMES)
        return [elemento.text for elemento in elementos_nombre]
    
    def continuar_comprando(self): #regresa a la página del inventario
        self.driver.find_element(*self._CONTINUE_SHOPPING).click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
    
    def proceder_checkout(self): #inicia proceso de checkout
        self.driver.find_element(*self._CHECKOUT_BUTTON).click()  #TODO REVISAR SE PUEDE DEVOLVER CHECKOUT PAGE
        return self