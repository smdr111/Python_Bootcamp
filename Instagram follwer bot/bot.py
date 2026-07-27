from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
import os
load_dotenv()

INST_EMAIL = os.getenv("INST_EMAIL")
INST_PASSWORD = os.getenv("INST_PASSWORD")
INST_LOGIN_URL = os.getenv("INST_LOGIN_URL")

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        # Get the Insta url
        self.driver.get(INST_LOGIN_URL)

        # Wait 2 sec and get hold of the input blocks
        sleep(2)
        email_input = self.driver.find_element(By.NAME,"username")
        password_input = self.driver.find_element(By.NAME,"password")
        login_btn = self.driver.find_element(By.XPATH,"/html/body/div/aside/div/form/button")

        # Fill the input blocks and click login
        email_input.send_keys(INST_EMAIL)
        password_input.send_keys(INST_PASSWORD)
        login_btn.click()

        # Save info btn
        sleep(2)
        save_info_btn = self.driver.find_element(By.XPATH,"//*[@id='popup-save-login']/div/div[2]")
        save_info_btn.click()

        # Turn on notifications btn
        sleep(1)
        notify_btn = self.driver.find_element(By.XPATH,"//*[@id='popup-notifications']/div/button[2]")
        notify_btn.click()

    def search(self,name):
        # Get the search input block and fill the profile info to be searched
        sleep(2)
        search_btn = self.driver.find_element(By.XPATH,"/html/body/div[1]/nav/button")
        search_btn.click()

        sleep(2)
        search_input = self.driver.find_element(By.XPATH,"/html/body/aside/div[2]/input")
        search_input.send_keys(name)
        sleep(1)
        search_input.send_keys(Keys.ENTER)

    def start_following(self):
        # Go to the profile follower page and start following to the accounts
        sleep(2)
        followers_btn = self.driver.find_element(By.XPATH,"/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a")
        followers_btn.click()

        # Get all the follow buttons of the accounts
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".followers-scroll button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                # An "Unfollow?" dialog opened (you already follow this account).
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()








