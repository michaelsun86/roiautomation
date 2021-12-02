import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.confest import setup
import time


@pytest.mark.usefixtures("setup")
class TestOne:

    def test_LoginPage(self, request):

        self.driver.find_element(By.ID, "email").send_keys("denni.qa@mailinator.com")
        time.sleep(3)
        self.driver.find_element(By.ID, "password").send_keys("0yoGd&5P")
        time.sleep(3)
        self.driver.find_element(By.ID, "login-btn").click()
        time.sleep(10)
        

        HomeText = self.driver.find_element(By.XPATH, "//div[@class='text-left pl-6-vh roi-dashboard-title col-12 col-md-6']/span").text
        assert ("Welcome to Roi-AI" in HomeText)