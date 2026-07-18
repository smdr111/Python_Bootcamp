from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page/")

num_articles = driver.find_element(By.CSS_SELECTOR,value='#mwDQ a')
#num_articles.click()

#Find element by link text
all_portals = driver.find_element(By.LINK_TEXT,value='Content portals')
#all_portals.click()

# Find search <input> by name
search  = driver.find_element(By.NAME,value='search')
#search.send_keys('Bitcoin',Keys.ENTER)
driver.quit()