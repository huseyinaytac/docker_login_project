import time
import colorama
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logs import logs_file
from colorama import Back,Fore,Style
colorama.init(autoreset=True)

log = logs_file.get_logs()


class selenium_helper:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):
        self.driver.get(page_url)

    def quit_driver(self):
        self.driver.quit()

    ## input ##
    def insert_text_in_input_filed(self, locator, input_text):
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).send_keys(input_text)
    ## click ##
    def click(self, locator):
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).click()


    def selector(self,selector,dom, contanis_text):
        btn = {f"{selector}": f"//{dom}[contains(text(),'{contanis_text}')]"}
        self.driver.find_element(list(btn.keys())[0], list(btn.values())[0])



    ##TestEquals##
    def is_text_equal(self, locator, text):
        try:
            text_equal=self.driver.find_element(list(locator.keys())[0], list(locator.values())[0])
            assert text_equal.text in text
            log.info(text_equal.text +  "-----"+"Metinsel ifade Birbirini Karşılamaktadır")
            print(Fore.GREEN+text_equal.text +  "-----"+"Metinsel ifade Birbirini Karşılamaktadır")
        except NoSuchElementException:
            log.error("Metinsel ifade Birbirini karşılamamaktadır.")
            print(Fore.YELLOW+"Metinsel ifade Birbirini karşılamamaktadır.")

    ##Displayed##
    def is_displayed(self, locator):
        try:
            displayed = self.driver.find_element(list(locator.keys())[0], list(locator.values())[0])
            assert displayed.is_displayed()
            log.info(displayed.text + "-----"+"Görüntülenir Öğe Mevcuttur.")
            print(Fore.GREEN+displayed.text + "-----"+"Görüntülenir Öğe Mevcuttur.")
        except NoSuchElementException:
            log.error("Görüntülenir Öğe Mevcut Değildir.")
            print(Fore.YELLOW+"Görüntülenir Öğe Mevcut Değildir.")

    ##Selected##
    def is_selected(self, locator):
        try:
            selected = self.driver.find_element(list(locator.keys())[0], list(locator.values())[0])
            assert selected.is_selected()
            log.info(selected.text + "-----"+"Seçilebilirlik Sağlanmıştır.")
            print(Fore.GREEN+selected.text + "-----"+"Seçilebilirlik Sağlanmıştır.")
        except NoSuchElementException:
            log.error("Seçilebilirlik Sağlanamamıştır.")
            print(Fore.YELLOW+"Seçilebilirlik Sağlanamamıştır.")


        ##ToastMessage##
    def toast_message(self, locator):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((list(locator.keys())[0], list(locator.values())[0])))


            toast_detail = self.driver.find_element(list(locator.keys())[0], list(locator.values())[0])
            log.info("Sistem tarafından verilen." + "-----" + toast_detail.text + "------" + "Mesaj Doğrudur.")
            print(Fore.GREEN+"Sistem tarafından verilen." + "-----" + toast_detail.text + "------" + "Mesaj Doğrudur.")
        except NoSuchElementException:
            log.error("Sistem tarafından verilen  mesajı hatalı gelmektedir.")
            print(Fore.YELLOW+"Sistem tarafından verilen  mesajı hatalı gelmektedir.")
            time.sleep(1)


    def toast_message_text_assertion(self, locator, text):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((list(locator.keys())[0], list(locator.values())[0])))

            toast_detail = self.driver.find_element(list(locator.keys())[0], list(locator.values())[0])
            assert text in toast_detail.text
            log.info("Sistem tarafından verilen" + "-----" + toast_detail.text + "------" + "Mesajı Doğrudur.")
            print(Fore.GREEN+"Sistem tarafından verilen" + "-----" + toast_detail.text + "------" + "Mesajı Doğrudur.")
        except NoSuchElementException:
            log.error("Sistem tarafından verilen  mesajı hatalı gelmektedir")
            print(Fore.YELLOW+"Sistem tarafından verilen  mesajı hatalı gelmektedir")
            time.sleep(1)

