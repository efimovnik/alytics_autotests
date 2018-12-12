import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ETHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self, project_id):
        wd = self.app.wd
        app = self.app
        app.open_home_page()
        if not (wd.current_url.endswith("https://testing.alytics.ru/projects/%s?items_on_page=20&page=1"%project_id)):
            WebDriverWait(wd, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/projects/%s')]" % project_id))
            )
            wd.find_element_by_xpath("//a[contains(@href, '/projects/%s')]" % project_id).click()

    def choose_shows_in_traffic_columns(self):
        wd = self.app.wd
        # open traffic column settings
        wd.find_element_by_xpath("//span/span/div").click()
        # select random checkbox
        wd.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()
        # save column settings changes
        wd.find_element_by_xpath("//div[2]/button[2]").click()

    def choose_random_parameter_in_traffic_columns(self):
        wd = self.app.wd
        # open traffic column settings
        wd.find_element_by_xpath("//span/span/div").click()
        # select random checkbox
        checkbox = random.randint(2, 10)
        wd.find_element_by_xpath("(//input[@type='checkbox'])[%s]" % checkbox).click()
        print(checkbox)
        # save column settings changes
        wd.find_element_by_xpath("//div[2]/button[2]").click()

    def get_column_count(self):
        wd = self.app.wd
        l = []
        for el in wd.find_elements_by_class_name("rt-th-header"):
            el.text.encode('utf-8')
            l.append(el)
        return len(l)

'''
String
metro = "";
WebElement getMetroStation = driver.findElement(
    By.xpath("//div[contains (@class, 'dropdown__item')]/span/span[text()='" + metro + "']"));
((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView();", getMetroStation);
getMetroStation.click();
'''

