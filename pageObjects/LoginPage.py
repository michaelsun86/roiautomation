from selenium.webdriver.common.by import By


class LoginPage:

    #def __init__(self, driver):
    #    self.driver = driver

    forgot = (By.ID, "forgot-password")
    remember = (By.ID, "checkbox-remember-me")
    email = (By.ID, "email")
    password = (By.ID, "password")
    submit = (By.ID, "login-btn")
    success = (By.XPATH, "//div[@class='sc-kDTinF fERnMN']/div[1]/div[1]/span")
    
    

    def getForgot(self):
        return self.driver.find_element(*LoginPage.forgot)

    def getEmail(self):
        return self.driver.find_element(*LoginPage.email)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getRemember(self):
        return self.driver.find_element(*LoginPage.remember)

    def getSubmit(self):
        return self.driver.find_element(*LoginPage.submit)
    
    def getSuccess(self):
        return self.driver.find_element(*LoginPage.success)
