def time_of_the_day(t):
    return 'AM' if t == 'PM' else 'PM'


def new_day(n, day, week_dict):
    for i in range(1, 8):
        if week_dict[i] == day:
            if (n + i) <= 7:
                key = n + i
            else:
                key = (n + i) % 7
            break
    return week_dict[key]


week_dict = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}


def add_time(start, duration, day=''):
    start_split = start.split(' ')
    start_time = start_split[0].split(':')
    duration_split = duration.split(':')
    day = day.lower()
    hours = int(duration_split[0]) + int(start_time[0])
    mins = int(duration_split[1]) + int(start_time[1])
    if mins < 10:
        mins = f'0{mins}'
    period = start_split[1]
    if int(mins) >= 60:
        hours += 1
        mins -= 60
        if mins < 10:
            mins = f'0{mins}'
    if hours < 24:
        if hours < 12:
            return f'{hours}:{mins} {period}, {day.capitalize()}' if day != '' else f'{hours}:{mins} {period}'
        else:
            remainder = hours % 12
            if remainder == 0:
                remainder = 12
            if period == 'AM':
                
                period = time_of_the_day(period)
                return f'{remainder}:{mins} {period}, {day.capitalize()}' if day != '' else f'{remainder}:{mins} {period}'
            else:
                
                period = time_of_the_day(period)
                return f'{remainder}:{mins} {period}, {day.capitalize()} (next day)' if day != '' else f'{remainder}:{mins} {period} (next day)'
    elif hours >= 24:
        remainder = hours % 12
        if remainder == 0:
            remainder = 12
        quotient = hours // 12
        if quotient % 2 != 0:
            period = time_of_the_day(period)
        no_of_days = (quotient // 2) + (quotient % 2)
        if no_of_days < 2:
            return f'{remainder}:{mins} {period}, {new_day(no_of_days, day.capitalize(), week_dict)} (next day)' if day != '' else f'{remainder}:{mins} {period} (next day)'
        if no_of_days >= 2:
            days_later = f'{no_of_days} days later'
        if day != '':
            new_time = f'{remainder}:{mins} {period}, {new_day(no_of_days, day.capitalize(), week_dict)} ({days_later})'
        else:
            new_time = f'{remainder}:{mins} {period} ({days_later})'
        return new_time


print(add_time("8:16 PM", "466:02", 'tuesday'))
