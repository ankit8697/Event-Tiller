from bs4 import BeautifulSoup
import requests

class CarletonEvent:
	def __init__(self):
		self.name = ''
		self.url = ''
		self.start_time = None
		self.end_time = None
		self.location = ''
		self.categories = []
		self.audiences = []
		
	def __repr__(self):
		return self.name+' '+self.url

def get_events_from_url(site_url = 'https://apps.carleton.edu/calendar/?view=daily'):
	'''
		Returns a list of CarletonEvent objects from the given Carleton Calendar link.
	'''
	
	site_req = requests.get(site_url)
	content = BeautifulSoup(site_req.content, 'html.parser')

	base_url = 'https://apps.carleton.edu/calendar/'
	all_events = []
	for element in content.find_all('li'):
		cur_class = element.get('class')
		if(cur_class == ['event', 'hasTime']): #iterates over the events on the day being looked at
			cur_event = CarletonEvent()
			print()	
			print('Title: '+element.a.text)
			cur_event.name = element.a.text
			print('URL: '+element.a.get('href'))
			
			event_url = base_url + element.a.get('href')
			cur_event.url = event_url
			event_req = requests.get(event_url)
			event_content = BeautifulSoup(event_req.content, 'html.parser')
			
			for event_element in event_content.find_all('span'):
				cur_class = event_element.get('class')
				if(cur_class == ['time']):
					print("Time: "+event_element.text)
					cur_event.time = event_element.text
				if(cur_class == ['location']):
					print("Location: "+event_element.text)
					cur_event.location = event_element.text
				
			for event_element in event_content.find_all('div'):
				cur_class = event_element.get('class')
				if(cur_class == ['categories']):
					categories = []
					for tag in event_element.find_all('a'):
						categories.append(tag.text)
					print("Categories: "+str(categories))
					cur_event.categories = categories
				if(cur_class == ['audiences']):
					audiences = []
					for tag in event_element.find_all('a'):
						audiences.append(tag.text)
					print("Audiences: "+str(audiences))
					cur_event.audiences = audiences
				
			all_events.append(cur_event)
			
	return all_events
	
def get_events_filtered(event_list, name = None, start_date_time = None, end_date_time = None, categories = []):
	final_list = []
	for cur_event in event_list:
		if name is not None:
			if cur_event.name != name:
				continue
		if start_date_time is not None:
			if cur_event.start_date_time < start_date_time:
				continue
		if end_date_time is not None:
			if cur_event.end_date_time > end_date_time:
				continue
		if len(categories) > 0:
			matching_tag = False
			for tag in cur_event.categories:
				if tag in categories:
					matching_tag = True
			if not matching_tag:
				continue
		
		final_list.append(cur_event)
	return final_list