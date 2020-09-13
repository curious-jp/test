from bs4 import BeautifulSoup
import urllib.request as req

url="https://info.finance.yahoo.co.jp/history/?code=USDJPY"

soup=BeautifulSoup(req.urlopen(url),'html.parser')
price=soup.select_one(".stoksPrice").string
print(price)

#this is test
