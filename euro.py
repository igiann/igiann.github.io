import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'https://www.bankofalbania.org/Tregjet/Kursi_zyrtar_i_kembimit/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"lxml")
table = soup.find_all('table')
rows = table[0].findChildren(['th', 'tr'])
euro = rows[4].findChildren('td')
print(euro[2].text)

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
url = 'http://iliria98.com/'
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need

soup = BeautifulSoup(data,"lxml")
table = soup.find_all("div", {"class": "line"})

x = table[2].findChildren('span')
sale = float(x[1].text)
buy = float(x[2].text)

print(sale)
print(buy)


