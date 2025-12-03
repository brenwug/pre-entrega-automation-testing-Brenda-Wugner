
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_login

CASOS_LOGIN = leer_csv_login("datos/login.csv") #importa los datos del archivo csv

@pytest.mark.parametrize("usuario, clave, debe_funcionar", CASOS_LOGIN)
def test_login(driver, usuario, clave, debe_funcionar):
    login = LoginPage(driver)

    login.abrir_pagina()

    login.completar_usuario(usuario)
    login.completar_clave(clave)
    login.hacer_clic_login()

    if debe_funcionar:
        # Login exitoso, valida inventario
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

        # Validar resultado /inventory.html
        assert "/inventory.html" in driver.current_url, "El login debería funcionar pero no redirigió al inventario"

        os.makedirs("reports", exist_ok=True)
        path = os.path.join("reports", f"login_ok_{usuario}.png")
        driver.save_screenshot(path)
        print(f"Login correcto con usuario {usuario}")
    
    else:
        #Login fallido con error visible
        assert login.esta_error_visible(), f"Se esperaba error con el usuario '{usuario}'"

        os.makedirs("reports", exist_ok=True)
        path = os.path.join("reports", f"login_error_{usuario}.png")
        driver.save_screenshot(path)
        print(f"Error correctamente mostrado para '{usuario}'")
