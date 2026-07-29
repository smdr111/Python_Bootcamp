from soup import CollectData
from bot import FormFiller
from time import sleep

# Get all the data using BeautifulSoup
data = CollectData()
addresses = data.get_address()
prices = data.get_price()
links = data.get_link()

# Fill the form using Selenium
bot = FormFiller()
for i in range(10):
    sleep(1)

    bot.fill_address(addresses[i])
    bot.fill_price(prices[i])
    bot.fill_link(links[i])

    bot.submit()
    bot.submit_new()

bot.quit()
