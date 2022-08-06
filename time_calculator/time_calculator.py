def add_time(start, duration, start_day):

    # Breaks down the start time
    start_comps = start.split()
    start_time = start_comps[0].split(':')
    if start_time[0][0] == "0" :
        start_time[0] = start_time[0][1]
    start_hour = int(start_time[0])
    start_minute = int(start_time[1])
    if start_comps[1].lower() == "pm" :
        start_hour = start_hour + 12
    start_time_mins = start_hour * 60 + start_minute
    if start_time_mins > 1440 :
        new_time = "Invalid start time input. Retry"
        return new_time

    # Breaks down the duration to be added
    duration_comps = duration.strip().split(':')
    duration_hour = int(duration_comps[0])
    duration_min = int(duration_comps[1])
    duration_time_mins = duration_hour * 60 + duration_min

    # Adds the start time in minutes and duration time in minutes together
    new_time_mins = start_time_mins + duration_time_mins
    days_later = int(new_time_mins / 1440)
    new_time_mins = new_time_mins - 1440 * days_later

    # Formats new time
    time_of_day = "AM"  
    new_hour_str = str()
    if new_time_mins / 60 > 12 :
        time_of_day = "PM"
        new_time_mins = new_time_mins - 720
    if new_time_mins > 59 :
        new_hour_str = str(int(new_time_mins / 60))
    else :
        new_hour_str = '12'
    
    new_minute_str = str()
    if new_time_mins % 60 < 10 :
        new_minute_str = "0" + str(new_time_mins % 60)
    else :
        new_minute_str = str(new_time_mins % 60)
    
    # Formats the 'days later' part of the string
    days_later_str = str()
    if days_later > 0 :
        if days_later == 1 :
            days_later_str = '(next day)'
        else :
            days_later_str = '(' + str(days_later) + ' days later)'

    # Calculates what day of the week the new day is on
    day_values = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 7
    }
  
    day_val = day_values.get(start_day.strip().lower(), -1)
    new_day_val = int()
    new_day_str = str()
    if day_val > 0 :
        day_val = day_val + days_later
        new_day_val = day_val % 7
        if new_day_val == 0 :
            new_day_str = "Sunday"
        elif new_day_val == 1 :
            new_day_str = "Monday"
        elif new_day_val == 2 :
            new_day_str = "Tuesday"    
        elif new_day_val == 3 :
            new_day_str = "Wednesday"
        elif new_day_val == 4 :
            new_day_str = "Thursday"
        elif new_day_val == 5 :
            new_day_str = "Friday"
        elif new_day_val == 6 :
            new_day_str = "Saturday"
    else :
        new_day_str = "Invalid Day"

          
    new_time = new_hour_str + ":" + new_minute_str + " " + time_of_day + " " + new_day_str + " " + days_later_str
    return new_time