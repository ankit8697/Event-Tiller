from bs4 import BeautifulSoup
import requests
import re

#site_url = input("Site url? ")
site_url = 'https://apps.carleton.edu/calendar/?view=daily&start_date=2019-04-13&no_search=1'
site_req = requests.get(site_url)
content = BeautifulSoup(site_req.content, 'html.parser')

for element in content.find_all('li'):
	cur_class = element.get('class')
	if(cur_class == ['event', 'hasTime']):
		print(element.a.text)
		print(element.a.get('href'))
		
	