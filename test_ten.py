import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestOne(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("disable-gpu")
        self.options.add_argument("headless")
        self.options.add_argument("no-default-browser-check")
        self.options.add_argument("no-first-run")
        self.options.add_argument("no-sandbox")
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities={
                "browserName": "chrome",
            })
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_one(self):
        driver = self.driver
        driver.get("site")
        sleep(10)
        login = driver.find_element_by_class_name('euiFieldText')
        login.send_keys('login')
        senha = driver.find_element_by_class_name('euiFieldPassword')
        senha.send_keys('senha%')
        logar = driver.find_element_by_xpath(
            '//*[@id="kibana-body"]/div/div[2]/div/div[2]/div/div/div/div/div/div/form/div[4]/div/button')
        logar.click()

        elemento = self.driver.find_element_by_link_text('EQCLB')
        elemento.click()

        menu = self.driver.find_element_by_xpath('//*[@id="kibana-body"]/div/header/div/div[1]/div[1]/button')
        menu.click()

        logs = self.driver.find_element_by_link_text('Logs')
        logs.click()

        search = self.driver.find_element_by_xpath(
            '//*[@id="kibana-body"]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div/input')
        search.send_keys('...*')
        search.send_keys(Keys.ENTER)

if __name__ == "__main__":
    unittest.main()
