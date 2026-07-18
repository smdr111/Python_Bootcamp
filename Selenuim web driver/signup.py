from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

name = driver.find_element(By.NAME,value='fName')
last_name = driver.find_element(By.NAME,value='lName')
email = driver.find_element(By.NAME,value='email')


name.send_keys('Samandar')
last_name.send_keys('Oripov')
email.send_keys('febwrjbfwqji@gmail.com')

submit = driver.find_element(By.CSS_SELECTOR,value='form button')
submit.click()

driver.quit()