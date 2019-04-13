from bs4 import BeautifulSoup
import requests
import re

#site_url = input("Site url? ")
site_url = 'https://apps.carleton.edu/calendar/?view=daily&start_date=2019-04-13&no_search=1'
site_req = requests.get(site_url)
content = BeautifulSoup(site_req.content, 'html.parser')

base_url = 'https://apps.carleton.edu/calendar/'
for element in content.find_all('li'):
	cur_class = element.get('class')
	if(cur_class == ['event', 'hasTime']):
		print()
		print('Title: '+element.a.text)
		print('URL: '+element.a.get('href'))
		
		event_url = base_url + element.a.get('href')
		event_req = requests.get(event_url)
		event_content = BeautifulSoup(event_req.content, 'html.parser')
		
		for event_element in event_content.find_all('span'):
			cur_class = event_element.get('class')
			if(cur_class == ['time']):
				print("Time: "+event_element.text)
			if(cur_class == ['location']):
				print("Location: "+event_element.text)
			
		for event_element in event_content.find_all('div'):
			cur_class = event_element.get('class')
			if(cur_class == ['categories']):
				categories = []
				for tag in event_element.find_all('a'):
					categories.append(tag.text)
				print("Categories: "+str(categories))
			if(cur_class == ['audiences']):
				audiences = []
				for tag in event_element.find_all('a'):
					audiences.append(tag.text)
				print("Audiences: "+str(audiences))
			
			