import pytest
from selenium import webdriver



@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="/Users/mikesunhaki/Documents/GaweanGS/Automation/ROI/chromedriver")
    driver.maximize_window()
    driver.get("https://staging.roi-ai.app/")
    request.cls.driver = driver
    yield
    driver.close()