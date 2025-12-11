import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options  
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
import os
from datetime import datetime

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    
    # Deshabilitar el gestor de contraseñas y notificaciones de seguridad
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "safebrowsing.enabled": False,
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    
    # Opciones de Selenium preexistentes
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.abrir_pagina().login_completo("standard_user", "secret_sauce")
    return driver

@pytest.fixture
def url_base_api():
    return "https://jsonplaceholder.typicode.com/users"

#hook de pytest para que tome screenshot cada vez que un test falla
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("login_in_driver") or item.funcargs.get("driver")
        if driver is None:
            return
        screenshots_dir = os.path.join("reports", "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = item.name
        filename = f"{test_name}_{timestamp}.png"

        file_path = os.path.join(screenshots_dir, filename)

        # Guardar screenshot
        driver.save_screenshot(file_path)
        print(f"Captura guardada: {file_path}")

        
        if pytest_html:
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(file_path))
                report.extra = extra