from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.config.settings import BASE_URL, PASSWORD, USERNAME
from src.utils.setup_driver import setup_driver


def login(driver, wait):
	# Abrir la web de inicio
	driver.get(BASE_URL)

	# Completar credenciales e iniciar sesion
	usuario = wait.until(EC.visibility_of_element_located((By.ID, 'user-name')))
	password = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
	boton_login = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))

	usuario.send_keys(USERNAME)
	password.send_keys(PASSWORD)
	boton_login.click()

	# Verificar el acceso al inventario
	assert '/inventory.html' in driver.current_url

	# Verificar logo y titulo
	logo = driver.find_element(By.CLASS_NAME, 'app_logo')
	assert logo.text == 'Swag Labs'

	titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
	assert titulo.text == 'Products'


def test_login():
	driver, wait = setup_driver(implicitly_wait=10, wait_timeout=10)

	try:
		login(driver, wait)
	finally:
		driver.quit()
