from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def setup_driver(implicitly_wait=0, wait_timeout=10):
	options = Options()

	# Clase personalizada para diferenciar de una instancia normal de Chrome
	options.add_argument('--class=selenium')

	driver = webdriver.Chrome(options=options)
	driver.implicitly_wait(implicitly_wait)

	wait = WebDriverWait(driver, wait_timeout) if wait_timeout > 0 else None

	return driver, wait
