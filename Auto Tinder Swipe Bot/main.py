from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,TimeoutException
from time import sleep

TINDER_URL = "https://tinder.com/"

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDER_URL)
wait = WebDriverWait(driver, 2)



sleep(2)
# Login Section
login_btn = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Log in")))
login_btn.click()

sleep(2)
iframe = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "iframe[id^='gsi_']")))
driver.switch_to.frame(iframe)
button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][aria-labelledby='button-label']")))
button.click()
driver.switch_to.default_content()

wait.until(lambda d: len(d.window_handles) > 1)
driver.switch_to.window(driver.window_handles[-1])

sleep(2)
email = wait.until(ec.element_to_be_clickable((By.ID, "identifierId")))
email.send_keys("your_email")

buttons = driver.find_elements(By.TAG_NAME, "button")
next_button = buttons[3]

buttons = driver.find_elements(By.TAG_NAME, "button")
driver.execute_script("arguments[0].click();", buttons[3])

sleep(2)
base_window = driver.window_handles[0]
driver.switch_to.default_content()

sleep(2)
like_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Like']]")))
for _ in range(20):
    sleep(1)
    try:
        like_btn.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)


driver.quit()