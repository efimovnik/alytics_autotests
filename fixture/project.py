from selenium.webdriver.support.ui import Select
from model.project import Project
import random


class ETHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self, project_id):
        wd = self.app.wd
        app = self.app
        app.open_home_page()
        if not (wd.current_url.endswith("https://testing.alytics.ru/projects/%s?items_on_page=20&page=1"%project_id)):
            wd.find_element_by_xpath("//a[contains(@href, '/projects/%s')]"%project_id).click()

    def choose_parameter_in_traffic_columns(self):
        wd = self.app.wd
        # open traffic column settings
        wd.find_element_by_xpath("//span/span/div").click()
        # select random checkbox
        checkbox = random.randint(2, 10)
        wd.find_element_by_xpath("(//input[@type='checkbox'])[%s]" % checkbox).click()
        print(checkbox)
        # save column settings changes
        wd.find_element_by_xpath("//div[2]/button[2]").click()

'''
String
metro = "";
WebElement getMetroStation = driver.findElement(
    By.xpath("//div[contains (@class, 'dropdown__item')]/span/span[text()='" + metro + "']"));
((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView();", getMetroStation);
getMetroStation.click();
'''

