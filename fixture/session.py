import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("login").clear()
        wd.find_element_by_name("login").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("div.userNav_user-dropdown-btn")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.userNav_user-dropdown-btn").click()
        return wd.find_element_by_css_selector("p.userNav_user-email.userNav_dropdown-title").text

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def logout(self):
        wd = self.app.wd
        # open user settings dropdown
        wd.find_element_by_xpath("//div[3]/div[2]/div").click()
        # click logout button
        time.sleep(1)
        wd.find_element_by_xpath("//div[2]/ul/li[3]/a/span").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()



