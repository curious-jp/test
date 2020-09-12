from bs4 import BeautifulSoup
import urllib.request as req
url="https://api.aoikujira.com/zip/xml/1930931"

#res=req.urlopen(url)
soup=BeautifulSoup(req.urlopen(url),'html.parser')

print(type(soup))
#print(soup)

#ken= soup.find("ken").string
#print(ken)
