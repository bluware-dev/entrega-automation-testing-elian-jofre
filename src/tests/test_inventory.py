from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.config.settings import BASE_URL, PASSWORD, USERNAME
from src.utils.setup_driver import setup_driver


def inventory(driver, wait):
	# Abrir la web e iniciar sesion
	driver.get(BASE_URL)

	usuario = wait.until(EC.visibility_of_element_located((By.ID, 'user-name')))
	password = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
	boton_login = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))

	usuario.send_keys(USERNAME)
	password.send_keys(PASSWORD)
	boton_login.click()

	# Esperar a que cargue el inventario
	wait.until(EC.url_contains('/inventory.html'))

	# Verificar titulo de la web
	assert driver.title == 'Swag Labs'

	# Verificar productos disponibles
	productos = wait.until(
		EC.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item'))
	)
	assert productos

	# Verificar nombre y precio del primer producto
	primer_producto = productos[0]

	nombre = primer_producto.find_element(By.CLASS_NAME, 'inventory_item_name')
	precio = primer_producto.find_element(By.CLASS_NAME, 'inventory_item_price')

	assert nombre.text == 'Sauce Labs Backpack'
	assert precio.text == '$29.99'

	# Verificar menu y filtro de productos
	assert driver.find_element(By.ID, 'react-burger-menu-btn').is_displayed()
	assert driver.find_element(By.CLASS_NAME, 'product_sort_container').is_displayed()


def test_inventory():
	driver, wait = setup_driver(implicitly_wait=10, wait_timeout=10)

	try:
		inventory(driver, wait)
	finally:
		driver.quit()
