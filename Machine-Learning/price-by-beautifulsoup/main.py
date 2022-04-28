import requests, pprint, os
from bs4 import BeautifulSoup

url = 'https://www.google.com/finance/quote/USD-JPY'
html = requests.get(url)
response_content = html.content
soup = BeautifulSoup(response_content, "html.parser")
usd_jpy = soup.find('div', class_="YMlKec fxKbKc").text
pprint.pprint(usd_jpy)