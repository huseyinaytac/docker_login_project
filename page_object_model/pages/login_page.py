import time
from helper.selenium_helper import  selenium_helper
from page_object_model.locators.login_locator import login_locator
from logs import logs_file

log = logs_file.get_logs()



class login_page:

    def __init__(self,driver):
        self.driver=driver


    def url_function(self,url):
        url_adres=selenium_helper(self.driver)
        url_adres.open_page(url)

    def username_function(self, username):
        user_name = selenium_helper(self.driver)
        user_name.insert_text_in_input_filed(login_locator.username,username)

    def password_function(self, password):
        user_password = selenium_helper(self.driver)
        user_password.insert_text_in_input_filed(login_locator.password,password)

    def login_btn_function(self):
        login_btn = selenium_helper(self.driver)
        login_btn.is_displayed(login_locator.giris_yap_btn)
        login_btn.click(login_locator.giris_yap_btn)

    def successfully(self,link_text):
        dashboard=selenium_helper(self.driver)
        dashboard.is_text_equal(login_locator.successfully,link_text)