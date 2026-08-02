from selenium.webdriver.chrome.webdriver import WebDriver #Importar webdriver para probar en el navegador
from pages.actions.register_actions import RegisterActions
from pytest_bdd import given, when, then, scenario
import allure

@scenario('register.feature', 'Register User with valid credentials')
@allure.suite('')
def test_register_user():
   pass

@given('The User goes to the website')
def step_open_web(driver) -> None:
   register = RegisterActions(driver)
   register.load("https://www.testertestarudo.com/es/sandbox")
   
@when('The User enters with valid credendials')
def step_register_user(driver) -> None:
   register = RegisterActions(driver)
   register.type_user("Daniel")
   register.type_email("email@testertestarudo.com")
   register.type_select_rol("QA Junior")
   register.type_checkbox()
   register.click_to_register()

@then('The User is registered succesfully')
def step_user_is_registred_succesfully(driver) -> None:
   register = RegisterActions(driver)
   register.user_is_logged()

