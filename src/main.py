from pathlib import Path

import pytest

Path('reports').mkdir(exist_ok=True)

if __name__ == '__main__':
	print('< Automation Tester CLI >')

	print('1. Ejecutar todos los tests')
	print('2. Login')
	print('3. Inventario')
	print('4. Carrito')

	option = input('Opción: ')

	tests = {
		'1': 'src/tests',
		'2': 'src/tests/test_login.py',
		'3': 'src/tests/test_inventory.py',
		'4': 'src/tests/test_cart.py',
	}

	if option in tests:
		pytest.main([tests[option]])
	else:
		print('Opción inválida')
