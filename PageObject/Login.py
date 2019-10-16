# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def Login_Text(Context):
    return Context.driver.find_element_by_id('i0116')
def Next_steps(Context):
    return Context.driver.find_element_by_id('idSIButton9')
def Assert_Loginame(Context,user):
    assert Context.driver.find_element_by_id('displayName').text==user
def Login_Password(Context):
    return Context.driver.find_element_by_id('i0118')
def Login_Button(Context):
    return  Context.driver.find_element_by_id('idSIButton9')
def Assert_Login_Success(Context,Loginusername):
    assert Context.driver.find_element_by_id('id_n').text==Loginusername
def WaitPsword(Context):
    WebDriverWait(Context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'i0118')))
def waitcheckUname(Context):
    WebDriverWait(Context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'id_n')))