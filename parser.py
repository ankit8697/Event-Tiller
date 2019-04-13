def parse_single_time(time, ampm):
    time_int = time.split(':')[0]*100 + time.split(':')[1]
    if ampm == 'am':
        return '{:04}'.format(str(time_int))
    elif ampm == 'pm':
        return '{:04}'.format(str(time_int + 1200))

def parse_time_range(time_string):
    time_components = time_string.split('–').rstrip().lstrip()
    
    if len(time_components) == 1:   # default event length 1 hr
        time1 = time_components[0].split(' ')
        start_time = parse_single_time(time1)
        end_time = str(int(start_time) + 100)
    
    else:
        time1 = time_components[0].split(' ')
        time2 = time_components[1].split(' ')
        if len(time1) == 1:
            time1[1] == time2[1]
        start_time = parse_single_time(time1)
        end_time = parse_single_time(time2)
    
    

def parse_date():
    pass

def main():
    sample = '11:00 am – 12:00 pm'

