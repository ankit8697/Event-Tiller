from bs4 import BeautifulSoup
import requests
import json
import parser

def make_event():
	'''
		Makes a Carleton Event dictionary, and initializes each field with default values.
		name: name of event
		url: url of event page
		start_time: datetime object representing the event's start time and date
		end_time: datetime object representing the event's end time and date
		location: 
	'''
	ev = {}
	ev['name'] = ''
	ev['url'] = ''
	ev['start_time'] = None
	ev['end_time'] = None
	ev['location'] = ''
	ev['categories'] = []
	ev['audiences'] = []
	return ev
	
def get_events_from_url(site_url = 'https://apps.carleton.edu/calendar/?view=daily'):
	'''
		Returns a list of dictionaries representing events at Carleton from the given Carleton Calendar link.
	'''
	
	site_req = requests.get(site_url)
	content = BeautifulSoup(site_req.content, 'html.parser')

	base_url = 'https://apps.carleton.edu/calendar/'
	all_events = []
	for element in content.find_all('li'):  #iterates over the events on the day being looked at
		cur_class = element.get('class')
		if(cur_class == ['event', 'hasTime']): #selects the html <li> tags that are actually events
			cur_event = make_event()
			cur_event['name'] = element.a.text
			
			event_url = base_url + element.a.get('href')
			cur_event['url'] = event_url
			event_req = requests.get(event_url) #makes a request to the individual event's page
			event_content = BeautifulSoup(event_req.content, 'html.parser')
			
			for event_element in event_content.find_all('span'): #gets information from the individual event's page
				cur_class = event_element.get('class')
				if(cur_class == ['time']):
					event_time_string = event_element.text
					event_times = parser.parse_datetime(cur_event['url'], event_time_string)
					cur_event['start_time'] = event_times[0]
					cur_event['end_time'] = event_times[1]
				if(cur_class == ['location']):
					cur_event['location'] = event_element.text
				
			for event_element in event_content.find_all('div'):
				cur_class = event_element.get('class')
				if(cur_class == ['categories']):
					categories = []
					for tag in event_element.find_all('a'):
						categories.append(tag.text)
					cur_event['categories'] = categories
				if(cur_class == ['audiences']):
					audiences = []
					for tag in event_element.find_all('a'):
						audiences.append(tag.text)
					cur_event['audiences'] = audiences
				
			all_events.append(cur_event)
			
	return all_events
	
def get_events_filtered(event_list, name = None, start_date_time = None, end_date_time = None, categories = []):
	final_list = []
	for cur_event in event_list:
		if name is not None:
			if cur_event['name'] != name:
				continue
		if start_date_time is not None:
			if cur_event['start_date_time'] < start_date_time:
				continue
		if end_date_time is not None:
			if cur_event['end_date_time'] > end_date_time:
				continue
		if len(categories) > 0:
			matching_tag = False
			for tag in cur_event['categories']:
				if tag in categories:
					matching_tag = True
			if not matching_tag:
				continue
		
		final_list.append(cur_event)
	return final_list
	
def event_list_to_json(event_list):
	event_list_iso_dates = []
	for ev in event_list:
		ev_iso_dates = ev.copy()
		if ev_iso_dates['start_time'] is not None:
			ev_iso_dates['start_time'] = ev_iso_dates['start_time'].isoformat()
		if ev_iso_dates['end_time'] is not None:
			ev_iso_dates['end_time'] = ev_iso_dates['end_time'].isoformat()
		event_list_iso_dates.append(ev_iso_dates)
	
	return json.dumps(event_list_iso_dates)

def event_list_to_json_file(event_list):
	json_info = event_list_to_json(event_list)
	f = open("event_data.json", "w")
	f.write(json_info)
	f.close()
	
def main():
	e = get_events_from_url();
	event_list_to_json_file(e)
	
if __name__ == "__main__":
	main()
	
