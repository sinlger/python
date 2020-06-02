from urllib.request import  urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
url = 'http://www.pythonscraping.com/pages/warandpeace.html'

html = urlopen(url)

bs = BeautifulSoup(html.read(),'html.parser')

nameList = bs.find_all('span',{'class','green'})

for name in nameList:
    print(name.get_text())