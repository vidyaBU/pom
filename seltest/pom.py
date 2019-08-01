from selenium import webdriver
from selenium.webdriver.common.by import By


class Login(object):

    def __init__(self,driver):
        self.driver=driver




    def UserName(self,user_name):
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "email").send_keys(user_name)


    def Password(self, password):

        self.driver.find_element(By.ID, "password").send_keys(password)


    def SignIn(self):
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "login").click()