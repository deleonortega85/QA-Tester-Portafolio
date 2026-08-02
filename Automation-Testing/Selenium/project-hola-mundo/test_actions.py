""" from selenium import webdriver #Importar webdriver para probar en el navegador
from selenium.webdriver.common.by import By # By sirve para buscar y seleccionar elementos
from selenium.webdriver.support.ui import Select # Sirve para tester de seleccion de combobox
import pytest #marco de trabajo de pruebas para Python que simplifica la creación de pruebas de código limpias, legibles y automáticas


@pytest.fixture #Capacidad de una funcion para que sea reutilizada dentro de un test.

def driver(): #Decorador
    driver = webdriver.Chrome() #Se selecciona el navegador a trabajar
    driver.get("https://www.testertestarudo.com/es/sandbox")
    yield driver # yield da la propiedad de ejecución para entrar y salir de las pruebas
    #3driver.refresh() #se actualiza la página como presionar F5
    #driver.implicitly_wait(10) #El tiempo de duración de una prueba
    assert "Tester Testarudo | Soluciones de testing para empresas – Capacitación QA profesional" in driver.title
    driver.quit() #cerrar el navegador o la prueba  

def test_click_element(driver): #función para testear sandboxlos click de un botón
    alert_button = driver.find_element(By.CLASS_NAME, "Sandbox-module__X_UfkW__sectionTag")
    alert_button.click()
    #alert = driver.switch_to.alert
    #alert.accept()

def test_fill_form(driver): #función para testear el llenado de campos
    name_input = driver.find_element(By.XPATH, "//input[@id='sb-name']")
    name_input.send_keys("Daniel")
    email_input = driver.find_element(By.XPATH, "//input[@id='sb-email']")
    email_input.send_keys("email@testertestarudo.com")
    role_input = Select(driver.find_element(By.ID, "sb-role"))
    role_input.select_by_visible_text("QA Junior")
    chequeo_input = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    if not chequeo_input.is_selected():
       chequeo_input.click()
    assert chequeo_input.is_selected()
    boton = driver.find_element(By.XPATH, "//input[@type='submit']")
    boton.click() """