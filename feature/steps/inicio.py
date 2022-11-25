from behave import given, when, then 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'entrar a la url {url}')
def step_impl(context, url):

    global driver

    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

@when(u'doy click en "iniciar seccion"')
def step_impl(context):

    btn_log_in = driver.find_element(By.CLASS_NAME, "my-account__desktop")
    btn_log_in.click()
    time.sleep(2)

@when(u'ingreso mi rut {rut}')
def step_impl(context, rut):

    insert_rut = driver.find_element(By.NAME, "ws_username")
    insert_rut.send_keys(rut)
    time.sleep(1)

@when(u'ingreso mi password {password}')
def step_impl(context, password):

    insert_password = driver.find_element(By.NAME, "password")
    insert_password.send_keys(password)
    time.sleep(1)

@when(u'doy click en "iniciar sesion"')
def step_impl(context):

    send = driver.find_element(By.XPATH, "//*[@id='inicio-sesion-ripley']")
    send.click()
    time.sleep(10)
    name = driver.find_element(By.CLASS_NAME, "my-account__box")
    print(name)

@then(u'cerrar secion')
def step_impl(context):
     
     closed = driver.find_element(By.XPATH, "//*[@id='ripley-sticky-header']/section/nav/ul/li[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/button")
     closed.click()
     time.sleep(5)
    
   