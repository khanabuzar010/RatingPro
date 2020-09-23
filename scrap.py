import requests
from bs4 import BeautifulSoup
URL = ' https://www.amazon.in/Test-Exclusive-606/dp/B07HGJK535/ref=lp_18589047031_1_3?s=electronics&ie=UTF8&qid=1579355407&sr=1-3'

headers = {"User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price =price[0:5]
print(converted_price)

print(title.strip())

