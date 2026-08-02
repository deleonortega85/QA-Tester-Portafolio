from selenium import webdriver #Importar webdriver para probar en el navegador
from selenium.webdriver.common.by import By # By sirve para buscar y seleccionar elementos
import pytest #marco de trabajo de pruebas para Python que simplifica la creación de pruebas de código limpias, legibles y automáticas


@pytest.fixture #Capacidad de una funcion para que sea reutilizada dentro de un test.

def driver(): #Decorador
    driver = webdriver.Chrome() #Se selecciona el navegador a trabajar
    driver.get("https://www.testertestarudo.com/es/sandbox")
    yield driver # yield da la propiedad de ejecución para entrar y salir de las pruebas
    assert "TGoogle" in driver.title
    driver.quit() #cerrar el navegador o la prueba  

def test_basic_web_actions(driver):
    driver.refresh() #
    driver.get()
    driver.back()
    driver.forward