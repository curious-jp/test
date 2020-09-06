import urllib.request

url="https://api.aoikujira.com/ip/ini"
res=urllib.request.urlopen(url)
data=res.read()

with open("data",mode="wb") as f:
	f.write(data)
	print("saved")

text=data.decode("utf-8")
print(text)