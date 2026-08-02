from selenium.webdriver.common.by import By

class Register():
    userInput = (By.XPATH, "//input[@id='sb-name']")
    emailInput = (By.XPATH, "//input[@id='sb-email']")
    roleSelect = (By.ID, "sb-role")
    chkboxChoose = (By.XPATH, "//input[@type='checkbox']")
    no_chkbox_message = "Debes aceptar los términos"
    registerButton = (By.XPATH, "//input[@type='submit']")
    userRegisterMessage = (By.XPATH, "//*[@id='form-result']")