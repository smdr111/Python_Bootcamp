import requests
from bs4 import BeautifulSoup
from messeger import NotificationManager

AMAZON_URL = """https://www.amazon.com/Instant-Pot-Electric-Multi-Cooker-Pressure/dp/B0B4PQDFCL/ref=sr_1_
1?crid=1Q7KR0RMV0BYH&dib=eyJ2IjoiMSJ9.szz0tNwle5nphvXcz0_M6R9RVQaL9FK0TL2EdVHtxKFthoB9Gld4td-Fu_enMclYIs
VVQEHDtbhKcjIECLp8ym18oGW-Hq-98TQsIrOAxc2HOK54SEjGv7JtteC9PTajBt8bUqEc8j1y-9KqmjanbyrF5kJZ2S1vDJIfaC91cx
AudSgC_M4rXdUlfUu3-jcIik5BgmQwnK5p57efSLCJW-SnOBi0BeXLhflnRkk3Qaw.o8RFPyQuoCoV-ztkk8QpQ5zTYJlDy40ijsg_S
OnChX4&dib_tag=se&keywords=instant%2Bpot&qid=1784047940&sprefix=insta%2Caps%2C120&sr=8-1&th=1"""

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\", \"Google Chrome\";v=\"150\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
}


response = requests.get(AMAZON_URL,headers=headers)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data,'html.parser')
price = float(soup.find(class_='aok-offscreen').get_text().split('$')[1])
title = soup.find(class_="a-size-large product-title-word-break").get_text().strip()

BUY_PRICE = 110

if price < BUY_PRICE:
    message = f"Subject:Amazon Price Alert!\n\n{title} is on sale for ${price}!\n{AMAZON_URL}".encode('utf-8')
    alert = NotificationManager()
    alert.send_email(to_email_address='oripovsamandar111@gmail.com',text=message)

