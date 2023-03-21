from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_webdriver(webdriver_type):
    # if webdriver_type == "firefox":
    #     driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
    # else:
    #     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # return driver

    # selenium_grid##
        options = webdriver.FirefoxOptions()
        driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                  desired_capabilities=DesiredCapabilities.FIREFOX, options=options)

        return driver






