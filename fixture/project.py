# -*- coding: utf-8 -*-
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

    # Column settings

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

    # Filter

    def filter_source_contains(self, source_name):
        wd = self.app.wd
        time.sleep(1)
        # launch the filter by click plus icon
        WebDriverWait(wd, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "i.fontello-plus")))
        wd.find_element_by_css_selector("i.fontello-plus").click()
        # select filter by source name
        WebDriverWait(wd, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form.rt-filterItem > div.ui-goal-select > "
                                         "div.ui-goal-select-surrogate > div.ui-goal-select-surrogate_value")))
        wd.find_element_by_css_selector("form.rt-filterItem > div.ui-goal-select > "
                                         "div.ui-goal-select-surrogate > div.ui-goal-select-surrogate_value").click()
        WebDriverWait(wd, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ui-goal-select-option_label")))
        wd.find_element_by_css_selector("div.ui-goal-select-option_label").click()
        # select operator 'contains'
        wd.find_element_by_xpath("//div[3]/div/div[2]/div/i").click()
        WebDriverWait(wd, 3).until(EC.element_to_be_clickable((By.ID, "react-select-3-option-2")))
        wd.find_element_by_id("react-select-3-option-2").click()
        # select source name
        wd.find_element_by_css_selector("input.rt-filterItem-input.default-text-input.valueInput").send_keys(source_name)
        # submit filtration
        WebDriverWait(wd, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#filter-actions > button.rt-blueBtn")))
        wd.find_element_by_css_selector("#filter-actions > button.rt-blueBtn").click()

    def get_sources_list(self):
        wd = self.app.wd
        sources = []
        time.sleep(1)
        for element in wd.find_elements_by_class_name("rt-data-rows"):
            name = element.find_element_by_tag_name("a").text
            sources.append(name)
        return sources



