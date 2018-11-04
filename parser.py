import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time

links = [
'https://prom.ua/Laminat', 
'https://na-pol.com.ua/laminat'
]
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

for link in links :
	try:
		r = requests.get(link, headers = headers)
	except:
		continue 
	r = str(r.text)
	soup = BeautifulSoup(r)
	title = soup.title.string;
	description = soup.find(attrs={"name":"description"})
	if title :
		texttitle = title
	else:
		texttitle = 'None'
	if description :
		textdescription = description['content']
	else:
		textdescription = 'None'
	print(link + '\t' + texttitle + '\t' + textdescription)
