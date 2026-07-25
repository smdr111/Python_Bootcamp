from bot import InternetSpeedTwitterBot

PROMISED_DOWN = 1000
PROMISED_UP = 1000


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
post = f"Hey Internet provider,why is my internet speed is down: {bot.down} up: {bot.up} when I pay for down:{PROMISED_DOWN}  up:{PROMISED_UP}"
bot.tweet_at_provider(post)
