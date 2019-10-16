# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def Open(Context):
    Context.driver.get('http://www.bing.com')
    Context.driver.maximize_window()
def Click_Login(Context):
    return Context.driver.find_element_by_id('id_l')
def Assert_LoginUI(Context,Keyword):
    assert Context.driver.page_source.__contains__(Keyword)
def WaitUI(Context):
    WebDriverWait(Context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'i0116')))
