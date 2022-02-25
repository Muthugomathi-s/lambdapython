from _ast import Assert

from lib2to3.pgen2 import driver
from threading import Thread

from selenium import webdriver

import time
import sys
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import unittest
import requests
import urllib3
import os
from os import environ
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.remote_connection import RemoteConnection

desired_cap =[
{'build':'Pythonlambada','platform' : 'Windows 10','browserName' : 'Chrome','version' :  "88.0",},
{'build':'Pythonlambada','platform' : 'macOS Sierra ','browserName' : 'MicrosoftEdge','version' :  "87.0",},

{'build':'Pythonlambada','platform' : 'Windows 7','browserName' : 'Firefox','version' :  "82.0",},

{'build':'Pythonlambada','platform' : 'Windows 10','browserName' : 'Internet Explorer','version' :  "11.0",}

]

url = "https://gomathiabi2000:WhzkcL3dvdA5Z54ESIk8QqsEqLIL3lPyF56uS2Xd18cVDiVtnZ@hub.lambdatest.com/wd/hub"

driver = webdriver.Remote(
    desired_capabilities=desired_cap,
    command_executor= url
)

def test_google_search():
        driver.get("https://www.lambdatest.com/selenium-playground")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_css_selector("span[class='cookie__bar__close hover:underline smtablet:hidden']").click()
        driver.find_element_by_xpath("//a[normalize-space()='Simple Form Demo']").click()
        time.sleep(2)

        assert "simple-form-demo" in driver.current_url

        message = "Welcome to LambdaTest"
        driver.find_element_by_id("user-message").send_keys(message)
        driver.find_element_by_id("showInput").click()
        time.sleep(2)
        Actualmsg = driver.find_element_by_xpath("//p[@id='message']").text
        if Actualmsg == message:
            print("Same message is displayed")
        else:
            print("Same message is not dispalyed")

        driver.close()
        print("First test case passed")

def test_lambdatest1_2():
        driver.get("https://www.lambdatest.com/selenium-playground")
        time.sleep(2)
        driver.find_element_by_css_selector("span[class='cookie__bar__close hover:underline smtablet:hidden']").click()

        driver.find_element_by_xpath("//a[normalize-space()='Drag & Drop Sliders']").click()
        time.sleep(2)

        e = driver.find_element_by_xpath("//div[@id='slider3']/div/input[@class='sp__range']")
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(e, 100, 2).perform()
        time.sleep(2)
        Currentrange = driver.find_element_by_xpath("//div[@id='slider3']/div/output[@id='rangeSuccess']").text
        if Currentrange == "95":
            print("Same range")
        else:
            print("Not in same range")
        driver.close()
        print("second test case passed")

def test_lambdatest1_3():

        driver.get("https://www.lambdatest.com/selenium-playground")
        time.sleep(2)

        driver.find_element_by_css_selector("span[class='cookie__bar__close hover:underline smtablet:hidden']").click()
        driver.find_element_by_xpath("//a[normalize-space()='Input Form Submit']").click()
        time.sleep(2)
        submitbtn = driver.find_element_by_css_selector("button[type='submit']")
        submitbtn.click()
        ele = driver.find_element_by_id("name")

        Actualwarning = driver.execute_script("return arguments[0].validationMessage;", ele)
        Expectedwarning = "Please fill out this field."
        if Actualwarning == Expectedwarning:
            print("Same warning is displayed")
        else:
            print("Same warning is not displayed")
        driver.find_element_by_xpath("//input[@placeholder='Name']").send_keys("Muthugomathi")
        driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("gomathiabi2000@gmai.com")
        driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("12356")
        driver.find_element_by_xpath("//input[@ placeholder='Company']").send_keys("cts")
        driver.find_element_by_xpath("//input[@placeholder='Website']").send_keys("www.cts.com")
        select = Select(driver.find_element_by_xpath("//select[@name='country']"))
        select.select_by_visible_text('United States')
        driver.find_element_by_xpath("//input[@ placeholder='City']").send_keys("Rajapalayam")
        driver.find_element_by_xpath("//input[@placeholder='Address 1']").send_keys("127/153 mukill vannam strt")
        driver.find_element_by_xpath("//input[@placeholder='Address 2']").send_keys("127/153 mukill vannam strt")
        driver.find_element_by_xpath("//input[@id='inputState']").send_keys("Tamilnadu")
        driver.find_element_by_id("inputZip").send_keys("626117")
        submitbtn = driver.find_element_by_css_selector("button[type='submit']")
        submitbtn.click()
        time.sleep(2)
        successmsg = driver.find_element_by_xpath("//p[@class='success-msg hidden']").text
        if successmsg == "Thanks for contacting us,we will get back to you shortly":
            print("Same text is displayed")
        else:
            print("Same text is not displayed")

        driver.close()
        print("Third test case passed")