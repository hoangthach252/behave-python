import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.constants import LINKEDIN_ACCOUNT


class DemoExamples4(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_example(self):
        wait = WebDriverWait(self.driver, 7)
        self.driver.get("https://www.linkedin.com/")
        # login_email = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-email')))
        login_email = self.driver.find_element(By.CLASS_NAME, 'login-email')
        login_email.send_keys(LINKEDIN_ACCOUNT['Thach Hoang']['USER_NAME'])

        # login_password = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-password')))
        login_password = self.driver.find_element(By.CLASS_NAME, 'login-password')
        login_password.send_keys(LINKEDIN_ACCOUNT['Thach Hoang']['PASSWORD'])

        # login_submit = wait.until(EC.element_to_be_clickable((By.ID, 'login-submit')))
        login_submit = self.driver.find_element(By.ID, 'login-submit')
        login_submit.click()

        start_time = time.time()
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.initial-load-animation:not(.fade-load)')))
        print("End test")
        print(time.time()-start_time)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
