from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfJvaQn19vzXrVaMlRvjvXe8u_11nYrGA2_V8dPET9zpzRrTQ/viewform?usp=header"

class FormFiller:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(FORM_URL)

    def fill_address(self,address):
        sleep(1)
        address_input = self.driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        address_input.send_keys(address)

    def fill_price(self,price):
        sleep(1)
        price_input = self.driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_input.send_keys(price)

    def fill_link(self,link):
        sleep(1)
        link_input = self.driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        link_input.send_keys(link)

    def submit(self):
        sleep(1)
        btn = self.driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
        btn.click()

    def submit_new(self):
        sleep(1)
        new_submit = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        new_submit.click()

    def quit(self):
        self.driver.quit()




