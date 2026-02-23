from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url: str):
        with allure.step(f"Открытие страницы {url}"):
            self.driver.get(url)

    def check_current_url(self, url: str) -> bool:
        with allure.step(f"Проверка, что текущий url равен {url}"):
            assert self.driver.current_url == url

    def get_locator(self, locator: tuple, nth: int = 0,):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        with allure.step(f"Генерация WebElement по локатору: {locator} с индексом={nth}"):
            return self.driver.find_elements(*locator)[nth]
    
    def click(self, locator: tuple, nth: int = 0):
        element = self.get_locator(locator=locator, nth=nth)
        with allure.step(f"Клик по элементу с локатором {locator} с индексом={nth}"):
            element.click()

    def check_visible(self, locator: str):
        element = self.get_locator(locator=locator)
        with allure.step(f"Проверка, что элемент с локатором: {locator} виден на странице"):
            assert element.is_displayed()

    def check_have_text(self, locator: str, text: str, nth: int = 0):
        element = self.get_locator(locator=locator, nth=nth)     
        with allure.step(f"Проверка, что элемент с локатором: {locator} с индексом={nth} имеет текст={text}"):
            assert element.text == text

    def scroll_to(self, locator: str):
        with allure.step(f"Скролл к элементу с локатором: {locator}"):
            self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def scroll_to_center(self, locator: str):
        with allure.step(f"Скролл к элементу с локатором: {locator} по центру"):
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", locator)

    def hide_scooter_image(self):
        with allure.step(f"Скрытие самоката на главной странице"):
            self.driver.execute_script("""
            var scooter = document.querySelector('div.Home_Scooter__3YdJy, div[class*="Home_Scooter"]');
            if(scooter) scooter.style.display = 'none';
            
            var blueprint = document.querySelector('div.Home_BluePrint__TGX2n, div[class*="Home_BluePrint"]');
            if(blueprint) blueprint.style.display = 'none';
        """)
    
    def fill(self, locator, text: str):
        with allure.step(f"Заполнение поля с локатором {locator} значением={text}"):
            element = self.get_locator(locator=locator)
            element.send_keys(text)

            assert element.get_attribute("value") == text

    
