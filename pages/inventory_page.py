from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']" ) #TODO VER SI CONVIENE POR CLASSNAME
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def obtener_titulo(self): #obtiene título de la página del inventario
        return self.driver.find_element(*self._TITLE).text
    
    def obtener_productos(self): #obtiene lista de productos
        return self.driver.find_elements(*self._PRODUCTS)

    def agregar_primer_producto(self): #Añade primer producto disponible al carrito
        primer_boton = self.driver.find_elements(*self._ADD_BUTTONS) [0]
        primer_boton.click()
        return self
    
    def obtener_contador_carrito(self): #obtiene número de productos en el carrito
        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        except:
            return 0
    
    def ir_al_carrito(self): #navega a la página del carrito
        self.driver.find_element(*self._CART_LINK).click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)
    
    def hacer_logout(self): #cierra la sesión del usuario
        self.driver.find_element(*self._MENU_BUTTON).click()
        logout_link = self.wait.until(
            EC.element_to_be_clickable(self._LOGOUT_LINK)
        )
        logout_link.click()
        from pages.login_page import LoginPage
        return LoginPage(self.driver)