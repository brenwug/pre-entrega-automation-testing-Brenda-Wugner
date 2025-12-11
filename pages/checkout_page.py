from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    # Locators
    _FIRST_NAME = (By.ID, "first-name")
    _LAST_NAME = (By.ID, "last-name")
    _ZIP_CODE = (By.ID, "postal-code")
    _CONTINUE_BUTTON = (By.ID, "continue")
    _FINISH_BUTTON = (By.ID, "finish")
    _COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.url_contains("checkout-step-one.html"))

    def completar_informacion_envio(self, nombre, apellido, zip_code):
        self.driver.find_element(*self._FIRST_NAME).send_keys(nombre)
        self.driver.find_element(*self._LAST_NAME).send_keys(apellido)
        self.driver.find_element(*self._ZIP_CODE).send_keys(zip_code)
        self.driver.find_element(*self._CONTINUE_BUTTON).click()
        self.wait.until(EC.url_contains("checkout-step-two.html")) # Esperar paso 2
        return self

    def finalizar_compra(self):
        self.driver.find_element(*self._FINISH_BUTTON).click()
        self.wait.until(EC.url_contains("checkout-complete.html"))
        return self

    def obtener_mensaje_confirmacion(self):
        return self.driver.find_element(*self._COMPLETE_HEADER).text
