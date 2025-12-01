Propósito del proyecto

Este proyecto automatiza pruebas funcionales básicas del sitio [SauceDemo](https://www.saucedemo.com/), incluyendo:
- Validación del login de usuarios.
- Navegación y verificación del catálogo de productos.
- Interacción con el carrito de compras, verificando que los productos se agreguen correctamente.
- Validación de elementos importantes como el menú de hamburguesa, el filtro de productos y el icono del carrito.

El objetivo es aplicar los contenidos aprendidos durante la primera mitad del curso de Testing Automatizado.

Tecnologías utilizadas
- Python (lenguaje de programación)
- Selenium (automatización de navegador)
- Pytest (framework de testing)
- WebDriver Manager (gestión automática del driver de Chrome)
- Pytest-html (generación de reportes HTML)
- Librerías estándar de Python: OS

Instalación de dependencias
1. Clonar el repositorio:
bash
git clone https://github.com/brenwug/pre-entrega-automation-testing-Brenda-Wugner.git
cd pre-entrega-automation-testing-Brenda-Wugner

Instalar dependencias con pip:
pip install selenium pytest webdriver-manager pytest-html

Ejecución de Pruebas:
Para ejecutar todos los tests ir al archivo run_tests.py y hacer clic en run python file, va a realizar las pruebas y generar un reporte html en la carpeta reports.

Todos los screenshots se guardan automáticamente en la carpeta prints/ para evidencia visual de las pruebas.
