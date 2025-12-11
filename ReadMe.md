# Propósito del proyecto

Este proyecto automatiza pruebas funcionales del sitio web SauceDemo (https://www.saucedemo.com/), y pruebas de API utilizando JSONPlaceholder.
Incluye validaciones de interfaz web con Selenium y validaciones de servicios REST con Requests.
El objetivo principal es aplicar los contenidos vistos en el curso de Testing Automatizado.

Incluye:
Pruebas de login (casos positivos y negativos).
Navegación y verificación del catálogo de productos.
Validación de productos utilizando datos en JSON.
Pruebas del carrito de compras.
Flujo básico de checkout.
Automatización de endpoints con métodos GET, POST y DELETE sobre JSONPlaceholder.
Capturas de pantalla automáticas cuando un test falla.
Generación de reportes HTML.

## Tecnologías Utilizadas
1. Python
2. Selenium WebDriver
3. Pytest
4. Requests
5. WebDriver Manager
6. Librerías estándar (os, json, csv, datetime)

## Instalación

### Clonar el repositorio:
git clone https://github.com/brenwug/pre-entrega-automation-testing-Brenda-Wugner.git
cd pre-entrega-automation-testing-Brenda-Wugner
### Crear entorno virtual (opcional):
python -m venv venv
### Activar:
Windows:
venv\Scripts\activate
Mac / Linux:
source venv/bin/activate
### Instalar dependencias:
pip install selenium pytest webdriver-manager pytest-html requests

## Ejecución de Pruebas
### Ejecutar toda la suite

La forma principal de correr todas las pruebas es mediante:
python run_tests.py
Este comando ejecuta todos los tests y genera el archivo:

reports/report.html

Ejecutar pytest directamente
pytest --html=reports/report.html --self-contained-html -v

Ejecutar tests individuales

Ejecutar solo login:

pytest tests/test_login.py


Ejecutar solo API:

pytest tests/test_api_jsonplaceholder.py

## Capturas de Pantalla

El proyecto incluye un hook en conftest.py que toma automáticamente capturas de pantalla cuando una prueba falla.
Estas imágenes se guardan en la carpeta:
reports/screenshots/
Además, las capturas se adjuntan dentro del reporte HTML.

## Pruebas Realizadas
- Pruebas UI (SauceDemo)
- Login con diferentes combinaciones desde archivo CSV.
- Validación del catálogo (título, productos, menú, filtro y carrito).
- Validación de productos usando datos externos desde JSON.
- Carrito: agregar y verificar productos.
- Checkout básico: completar datos y validar el mensaje de finalización.
- Pruebas API (JSONPlaceholder)
GET para obtener un usuario.
POST para crear un recurso.
DELETE para eliminar un recurso.
- Validación de códigos de estado y estructura JSON.

## Reporte de Pruebas

Al finalizar la ejecución, el reporte se genera automáticamente como:
reports/report.html
Incluye resultados de cada test y su duración.