# -*- coding: utf-8 -*-
import time

def test_column_settings_all_sources(app):
    app.open_home_page()
    # go to test project efficient table
    app.wd.find_element_by_xpath("//a[contains(text(),'UI table autotest')]").click()
    # open traffic column settings
    app.wd.find_element_by_xpath("//span/span/div").click()
    # select click's checkbox
    app.wd.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()
    # save column settings changes
    time.sleep(1)
    app.wd.find_element_by_xpath("//div[2]/button[2]").click()

