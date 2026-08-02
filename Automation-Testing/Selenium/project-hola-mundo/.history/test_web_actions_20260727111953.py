from selenium import webdriver #Importar webdriver para probar en el navegador
#from selenium.webdriver.common.by import By # By sirve para buscar y seleccionar elementos
from selenium.webdriver.chrome.options import Options # Poder inyectar un contexto dentro del Webdriver configurado
import pytest #marco de trabajo de pruebas para Python que simplifica la creación de pruebas de código limpias, legibles y automáticas


@pytest.fixture #Capacidad de una funcion para que sea reutilizada dentro de un test.

def driver(): #Decorador
    chrome_options = Options()
    chrome_options.add_argument("--headless") #Para añadir argumentos que no se vea
    c
    driver = webdriver.Chrome(options=chrome_options) #Se pueda reconocer las ordenes de webdriver
    driver.get("https://www.testertestarudo.com/es/sandbox")
    yield driver # yield da la propiedad de ejecución para entrar y salir de las pruebas
    assert "Google" in driver.title
    driver.quit() #cerrar el navegador o la prueba  

def test_basic_web_actions(driver):
    driver.refresh() #
    driver.get("https://www.google.com")
    driver.back()
    driver.forward()