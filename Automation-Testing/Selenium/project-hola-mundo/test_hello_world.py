""" from selenium import webdriver #Importar webdriver para probar en el navegador
from selenium.webdriver.common.by import By # By sirve para buscar y seleccionar elementos
import pytest #marco de trabajo de pruebas para Python que simplifica la creación de pruebas de código limpias, legibles y automáticas


@pytest.fixture #Capacidad de una funcion para que sea reutilizada dentro de un test.

def driver(): #Decorador
    driver = webdriver.Chrome() #Se selecciona el navegador a trabajar
    yield driver # yield da la propiedad de ejecución para entrar y salir de las pruebas
    #3driver.refresh() #se actualiza la página como presionar F5
    #driver.implicitly_wait(10) #El tiempo de duración de una prueba
    driver.quit() #cerrar el navegador o la prueba

def test_testertestarudo(driver): #Función para hacer la prueba automatizada
    driver.get("https://www.testertestarudo.com") #Se ubica el url de la web a probar o automatizar
    assert "Tester Testarudo | Soluciones de testing para empresas – Capacitación QA profesional" in driver.title #Comprueba que el título de la página sea el mismo
    #pytest: rastrear nuestro proyecto para ver si hay un test que nos dice si esta correcto o fallo el test

def tester_visit_google(driver): #Función para testear google
    driver.get("https://www.google.com") #Se ubica el url de la web a probar o automatizar
    assert "Google" in driver.title #Comprueba que el título de la página sea el mismo
    #pytest: rastrear nuestro proyecto para ver si hay un test que nos dice si esta correcto o fallo el test

def test_visit_sandbox_and_explore_elements(driver): #función para testear sandbox
    driver.get("https://www.testertestarudo.com/es/sandbox")
    driver.find_element(By.XPATH, "//input[@id='sb-name']")
    driver.find_element(By.CSS_SELECTOR, "input#sb-name")
    driver.find_element(By.ID, "sb-email")
    driver.find_element(By.CLASS_NAME, "Sandbox-module__X_UfkW__topbarTitle")

    driver.find_element(By.LINK_TEXT, "YouTube")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Capacitaciones")
    assert "Tester Testarudo | Soluciones de testing para empresas – Capacitación QA profesional" in driver.title """