from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # -------------- Common Interactions --------------

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def type(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def wait_for_elements(self, locator, expected_count=None, timeout=10, condition=EC.visibility_of_all_elements_located):
        
        try:

            if expected_count is not None:
                WebDriverWait(self.driver, timeout).until(
                    lambda driver: len(self.driver.find_elements(*locator)) == expected_count
                )

                elements = self.driver.find_elements(*locator)
                
                if len(elements) != expected_count:
                    raise TimeoutException(f"Expected {expected_count} elements, but found {len(elements)} elements.")
            
            return elements

        except TimeoutException as e:
            raise  
        except Exception as e:
            raise 
    
    def wait_for_element_invisibility(self, locator, timeout=10):
        """
        Wait for an element to become invisible.
        
        :param locator: The locator of the element (e.g., (By.XPATH, '...'))
        :param timeout: The maximum time to wait for the element to be invisible (default is 10 seconds).
        """
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            print(f"Timed out waiting for {locator} to become invisible.")
            return False
        return True
    
    def wait_until_visible(self, locator, timeout=10):
        """
        Wait until an element is visible on the page.
        :param locator: tuple (By.X, "value")
        :param timeout: max wait time in seconds
        :return: True if visible, False if timeout
        """
        print(f"Waiting for element to be visible: {locator}")
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            print(f"Element {locator} is now visible.")
            return True
        except Exception as e:
            print(f"Element {locator} was not visible after {timeout} seconds.")
            print(f"Error: {str(e)}")
            return False