from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    #URL de la página de login
    URL = "https://www.saucedemo.com/"

    # LOCATORS
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID,  "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-yrdy='error']")

    def __init__(self, driver):
        #Recibe instancia de Webdriver
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    
    def abrir(self):
        self.driver.get(self.URL) #Carga la URL en el navegador
        return self
    
    def completar_usuario(self, usuario: str):
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT)) #Ecribe el nombre de usuario
        campo.clear()  #Limpia antes de escribir
        campo.send_keys(usuario)
        return self
    
    def completar_clave(self, clave: str):
        campo = self.wait.until(
            EC.visibility_of_element_located(self._PASS_INPUT) #Escribe contraseña
        )
        campo.clear()
        campo.send_keys(clave)
        return self
    
    def hacer_clic_login(self):
        #Hace clic en el botón login
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self
    
    def login_completo(self, usuario, clave): #metodo para hacer login completo
        self.completar_usuario(usuario)
        self.completar_clave(clave)
        self.hacer_clic_login()
        return self
    
    def esta_error_visible(self) -> bool: #Comprueba si aparece mensaje de error en la pagina por login fallido
        try:
            self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
            return True
        except:
            return False
            
    def obtener_mensaje_error(self) -> str:
        if self.esta_error_visible():
            return self.driver.find_element(*self._ERROR_MESSAGE).text
        return ""