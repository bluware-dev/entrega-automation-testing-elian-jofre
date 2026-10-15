# Automation Testing: Pytest + Selenium

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Pytest-Testing-0A9EDC?logo=pytest&logoColor=white" alt="Pytest Badge">
  <img src="https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white" alt="Selenium Badge">
</p>

<p align="center">
  <em>Proyecto de automatización de pruebas web con Python, Pytest y Selenium WebDriver, aplicado a SauceDemo.</em>
</p>

---

<h3 align="center">Características</h3>

- **Pytest:** ejecución y organización de pruebas automatizadas.
- **Selenium WebDriver:** interacción y validación de interfaces web.
- **Configuración centralizada:** gestión de drivers y parámetros de testing.
- **Utilidades reutilizables:** handlers, utilidades y estructuras.
- **Reportes y evidencias:** soporte para resultados de ejecución y diagnóstico.

---

<h3 align="center">Estructura del proyecto</h3>

```text
automation-testing/
├── pyproject.toml
├── pytest.ini
├── README.md
├── TODO.md
├── reports/       # Reportes HTML
└── src/
    ├── config/    # Configuración del proyecto
    ├── main.py    # Punto de entrada
    ├── tests/     # Pruebas automatizadas
    └── utils/     # Configuración y utilidades del driver
```

```
# Instalar dependencias del proyecto
pip install -e .

# Ejecutar las pruebas
pytest -v

# Generar un reporte HTML
pytest -v --html=reports/reporte.html --self-contained-html
```

`main.py` funciona como un punto de entrada alternativo para ejecutar Pytest con una interfaz simple.

```
python -m src.main 
```