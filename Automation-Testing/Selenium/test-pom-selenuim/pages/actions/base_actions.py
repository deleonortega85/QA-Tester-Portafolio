from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BaseActions:
    
    def __init__(self, driver):
        self.driver = driver
    
    def load(self, url):
        self.driver.get(url)
        
    def _wait_for_element(self, by_locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(by_locator)
            )
            return self.driver.find_element(*by_locator)
        except TimeoutException:
            print("El elemento no fue encontrado")
            return None
        
    def element_click(self, by_locator):
        try: 
            user = self._wait_for_element(by_locator)
            if user:
                user.click()
            else:
                return "Can't click on the element"
        except Exception:
            return "Can't find in the element"
    
    def type_info(self, by_locator, keyword):
        user = self._wait_for_element(by_locator)
        if user:
            user.send_keys(keyword)
        else:
            raise Exception("Can't find in the element")   
    
    def chkbox_select(self, by_locator)-> bool:
        chkbox = self._wait_for_element(by_locator)
        if not chkbox.is_selected():
            chkbox.click()
        else:
            return False         
        
    def is_displayed(self, by_locator)-> bool:
            user = self._wait_for_element(by_locator)
            if user:
                user.is_displayed()
            else:
                return False   
    
    def is_enabled(self, by_locator)-> bool:
            user = self._wait_for_element(by_locator)
            if user:
                user.is_enabled()
            else:
                return False  