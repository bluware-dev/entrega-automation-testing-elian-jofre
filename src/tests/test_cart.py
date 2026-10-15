from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.config.settings import BASE_URL, PASSWORD, USERNAME
from src.utils.setup_driver import setup_driver


def cart(driver, wait):
	# Abrir la web e iniciar sesion
	driver.get(BASE_URL)

	usuario = wait.until(EC.visibility_of_element_located((By.ID, 'user-name')))
	password = driver.find_element(By.ID, 'password')
	boton_login = driver.find_element(By.ID, 'login-button')

	usuario.send_keys(USERNAME)
	password.send_keys(PASSWORD)
	boton_login.click()

	# Obtener primer producto del inventario
	primer_producto = wait.until(
		EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_item'))
	)

	# Guardar nombre y localizar boton
	nombre_producto = primer_producto.find_element(
		By.CLASS_NAME, 'inventory_item_name'
	).text
	boton_agregar = primer_producto.find_element(By.TAG_NAME, 'button')

	# Agregar producto y verificar contador
	boton_agregar.click()

	contador_carrito = wait.until(
		EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))
	)
	assert contador_carrito.text == '1'

	# Abrir carrito y verificar producto agregado
	wait.until(
		EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))
	).click()

	nombre_producto_carrito = wait.until(
		EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_item_name'))
	).text

	assert nombre_producto == nombre_producto_carrito


def test_cart():
	driver, wait = setup_driver(implicitly_wait=10, wait_timeout=10)

	try:
		cart(driver, wait)
	finally:
		driver.quit()
