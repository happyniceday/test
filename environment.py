# coding=utf-8
from selenium import webdriver
def before_all(Context):
    Context.driver=webdriver.Chrome('driver/chromedriver')
#def after_all(Context):
#    Context.driver.quit()
