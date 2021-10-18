# -*- coding:utf8 -*-
from time import sleep

from selenium import webdriver


class WebDemo:
    driver = webdriver.Chrome()
    driver.maximize_window()

    def open(self,**kwargs):
        self.driver.get(kwargs['txt'])
    def locator(self,**kwargs):
        return self.driver.find_element(kwargs['name'],kwargs['value'])
    def input(self,**kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])
    def click(self,**kwargs):
        self.locator(**kwargs).click()
    def wait(self,**kwargs):
        sleep(kwargs['txt'])
    def quit(self,**kwargs):
        self.driver.quit()


