import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = "https://sv.wikipedia.org/wiki/bilar"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
strings = []
substring = "bil"


for str in soup.findAll('a') :
    
    print(soup)
    if substring in str:
        print(soup)
    

