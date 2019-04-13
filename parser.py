import sys
import datetime as dt


def parse_single_time(time):
    time_components = time.split(' ')
    time_str = time_components[0]
    ampm = time_components[1]

    hour = int(time_str.split(':')[0])
    minute = int(time_str.split(':')[1])

    time_int = hour*100 + minute

    if ampm == 'am':
        return '{:04}'.format(time_int)
    elif ampm == 'pm':
        return '{:04}'.format(time_int%1200 + 1200)


def parse_time_range(time_string, start_date):
    time_components = time_string.split('–')    
    for i in range(len(time_components)):
        time_components[i] = time_components[i].rstrip().lstrip()

    if len(time_components) == 1:   # default event length 1 hr
        time1 = time_components[0]
        start_str = parse_single_time(time1)
        end_str = str(int(start_time) + 100)
    
    else:
        time1_components = time_components[0].split(' ')
        time2_components = time_components[1].split(' ')
        
        if len(time1_components) == 1:
            time1_components.append(time2_components[1])
        
        time1 = time1_components[0] + ' ' + time1_components[1]
        time2 = time2_components[0] + ' ' + time2_components[1]

        start_str = parse_single_time(time1)
        end_str = parse_single_time(time2)

    start_hr = int(start_str[:2])
    start_min = int(start_str[2:])

    end_hr = int(end_str[:2])
    end_min = int(end_str[2:])
    
    start_time = dt.time(hour=start_hr, minute=start_min)
    end_time = dt.time(hour=end_hr, minute=end_min)

    if end_time < start_time:
        day_shift = dt.timedelta(days=1)
        end_date = start_date + day_shift
    else:
        end_date = start_date

    return start_date, start_time, end_date, end_time


def parse_date_from_url(url):
    date_str = url[-10:]
    date_components = date_str.split('-')
    return date_components


def parse_datetime(url, time_string):
    year_str, month_str, day_str = parse_date_from_url(url)
    year = int(year_str)
    month = int(month_str)
    day = int(day_str)
    start_date = dt.date(year, month, day)

    start_date, start_time, end_date, end_time = parse_time_range(time_string, start_date)

    start_yr = start_date.year
    start_mon = start_date.month
    start_day = start_date.day
    start_hr = start_time.hour
    start_min = start_time.minute

    start_datetime = dt.datetime(start_yr, start_mon, start_day, hour=start_hr, minute=start_min)

    end_yr = end_date.year
    end_mon = end_date.month
    end_day = end_date.day
    end_hr = end_time.hour
    end_min = end_time.minute

    end_datetime = dt.datetime(end_yr, end_mon, end_day, hour=end_hr, minute=end_min)

    return tuple([start_datetime, end_datetime])


def tester():
    url = '?view=monthly&start_date=2019-04-13&event_id=1774519&date=2019-04-13'
    raw_time = '10:30 pm – 1:00 am'
    datetime_tuple = parse_datetime(url, raw_time)
    print(datetime_tuple)


if __name__ == '__main__':
    tester()
