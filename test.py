import urllib.request
import urllib.parse

API="https://api.aoikujira.com/zip/xml/get.php"

url="https://uta.pw/shodou/img/28/214.png"

values={
	'fmt':'xml',
	'zn':'1930931'
}
params=urllib.parse.urlencode(values)

url=API+"?"+params
print("url=",url)

data=urllib.request.urlopen(url).read()
text=data.decode("utf-8")
print(text)
