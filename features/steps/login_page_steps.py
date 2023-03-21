import time
import colorama
from behave import *
from logs import logs_file
from page_object_model.pages.login_page import login_page
from page_object_model.locators.login_locator import login_locator
from colorama import Back,Fore,Style
colorama.init(autoreset=True)
use_step_matcher("re")

log =logs_file.get_logs()



@given('Kullanici Uygulamanin Url "(.*)" Adresini gider')
def step_impl(context, url):
    url_adress=login_page(context.driver)
    url_adress.url_function(url)
    log.info("Uygulamanın Url Adresi"+"-----"+url)
    print(Fore.GREEN + "Uygulamanin Url Adresi"+"-----"+url)
    time.sleep(2)


@when('Kullanici UserName "(.*)" girer')
def step_impl(context, username):
    user_name=login_page(context.driver)
    user_name.username_function(username)
    log.info("Kullanıcı Adı"+"-----"+username)
    print(Fore.GREEN +"Kullanici Adi"+"-----"+username)
    time.sleep(2)

@step('Kullanici Password "(.*)" girer')
def step_impl(context, password):
    pass_word=login_page(context.driver)
    pass_word.password_function(password)
    log.info("Kullanıcı Şifresi"+"-----"+password)
    print(Fore.GREEN +"Kullanici sifresi"+"-----"+password)
    time.sleep(2)

@step("Kullanici Giris Yap butonuna tiklar")
def step_impl(context):
    login=login_page(context.driver)
    login.login_btn_function()
    time.sleep(2)

@then("Kullanicinin Uygulamaya giris yaptigi gorulur")
def step_impl(context):
    successfully=login_page(context.driver)
    successfully.successfully(login_locator.beklenen_cvp)
    log.error("Giriş Sağlanamadı")
    print(Fore.YELLOW +"Giris Saglanamadi")
    time.sleep(2)

