from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
load_dotenv()

Y_EMAIL = os.getenv("Y_EMAIL")
Y_PASSWORD = os.getenv("Y_PASSWORD")
Y_LOGIN_URL = os.getenv("Y_LOGIN_URL")
SPEED_TEST_URL = "https://www.speedtest.net/"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        self.chrome_options.add_argument(f"--user-data-dir={self.user_data_dir}")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)

        #Click go button
        sleep(2)
        go_btn = self.driver.find_element(By.XPATH,"//button[.//h1[text()='GO']]")
        go_btn.click()

        # Wait for the results and get them
        sleep(50)
        self.down = self.driver.find_element(By.XPATH,"//p[starts-with(normalize-space(), 'Download')]/following-sibling::h3").text
        self.up = self.driver.find_element(By.XPATH, "//p[starts-with(normalize-space(), 'Upload')]/following-sibling::h3").text



    def tweet_at_provider(self,post_text):
        self.driver.get(Y_LOGIN_URL)

        #Get the email and password input blocks
        sleep(2)
        email_input = self.driver.find_element(By.ID,'email')
        password_input =  self.driver.find_element(By.ID,'password')

        #Fill up the blocks
        email_input.send_keys(Y_EMAIL)
        password_input.send_keys(Y_PASSWORD)
        login_btn = self.driver.find_element(By.XPATH,"/html/body/div/div/form/button")
        login_btn.click()

        sleep(1)
        post_input = self.driver.find_element(By.XPATH,"//*[@id='tweet-compose']")
        post_input.send_keys(post_text)

        sleep(1)
        post_btn = self.driver.find_element(By.XPATH,"//*[@id='post-btn']")
        post_btn.click()
