from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración de las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Iniciar Chrome maximizado
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument("--headless")  # Ejecutar en modo headless si es necesario

# Ruta al ChromeDriver
chromedriver_path = r'C:\\Users\\user\\Desktop\\Codigos\\CursoPy\\CursoPython_Final\\chromedriver.exe'

# Inicializa el servicio de ChromeDriver
service = Service(chromedriver_path)

# Crea una instancia del navegador Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Abre la URL de login
    driver.get('https://jaguarete.unida.edu.py/jaguarete/Login')

    # Espera hasta que el campo de código esté presente y envía el código
    codigo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'codigo'))
    )
    codigo.send_keys("2022101401")

    # Espera hasta que el campo de contraseña esté presente y envía la contraseña
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password.send_keys("763254")

    # Espera hasta que el botón de login esté presente y hace clic
    login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[text()="Ingresar"]'))
    )
    login.click()

    # Espera unos segundos para que la página cargue después del login
    WebDriverWait(driver, 10).until(
        EC.url_changes('https://jaguarete.unida.edu.py/jaguarete/Login')
    )

except Exception as e:
    print(f"Ocurrió un error: {str(e)}")

finally:
    # Cierra el navegador
    driver.quit()
