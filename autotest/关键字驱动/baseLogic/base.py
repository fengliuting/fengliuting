# -*- coding:utf8 -*-
from time import sleep

from selenium import webdriver

# 基于type生成对应的浏览器对象
def browser(type_):
    try:
        driver = getattr(webdriver,type_)()
        driver.maximize_window()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome().maximize_window()
    return driver


class WebDemo:
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # 构造函数
    def __init__(self,type_):
        self.driver= browser(type_)

    def open(self,url):
        self.driver.get(url)
    def locator(self,name,value):
        return self.driver.find_element(name,value)
    def input(self,name,value,txt):
        self.locator(name,value).send_keys(txt)
    def click(self,name,value):
        self.locator(name,value).click()
    def wait(self,txt):
        sleep(txt)
    def clean(self,name,value):
        self.locator(name,value).clear()
    def quit(self):
        self.driver.quit()


