# coding=utf-8
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

import PageObject.Login as Login
import PageObject.LoginUI as LoginUI
from selenium.webdriver.support import expected_conditions as EC

@step(u'我在"{Keyword}"界面时')
def step_impl(Context,Keyword):
    LoginUI.Open(Context)
    LoginUI.Click_Login(Context).click()
    LoginUI.WaitUI(Context)
    LoginUI.Assert_LoginUI(Context,Keyword)

@step(u'我填写正确的"{user}"和"{password}"')
def step_impl(Context,user,password):
    Login.Login_Text(Context).clear()
    Login.Login_Text(Context).send_keys(user)
    Login.Next_steps(Context).click()
    Login.WaitPsword(Context)
    Login.Login_Password(Context).clear()
    Login.Login_Password(Context).send_keys(password)
    Login.Login_Button(Context).click()
@step(u'我将看见我的登录名是"{Loginusername}"')
def step_impl(Context,Loginusername):
    Login.waitcheckUname(Context)
    Login.Assert_Login_Success(Context,Loginusername)
