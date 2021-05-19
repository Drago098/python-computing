def add_time(start, duration, day=None):

    modifiers_later = 0
    days_later = 0

    days_of_week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
        ]
    
    modifier = start.split(" ")[1]
    initial_modifier = modifier

    start = start.split(" ")
    start.pop(1)
    start = ''.join(start)
    
    hour = int(start.split(":")[0]) + int(duration.split(":")[0])
    minute = int(start.split(":")[1]) + int(duration.split(":")[1])

    if minute > 59:
        minute -= 60
        hour += 1
    
    hour_modifier = hour

    while hour > 12:
        hour -= 12

    while hour_modifier > 11:
        hour_modifier -= 12
        modifier = "PM" if modifier == "AM" else "AM"
        modifiers_later += 1

    if modifiers_later % 2 != 0: #syntax from Beau, means if the modifier is not even (i.e. AM - PM - AM)
        if initial_modifier == "PM":
            modifiers_later += 1
        else:
            modifiers_later -= 1

    days_later = modifiers_later/2

    new_time = f"{hour}:{str(minute).zfill(2)} {modifier}"

    #logic from Beau for most part, code original+snippets from Beau
    if day:
        weekday = days_of_week.index(day.title())
        weekday_new = int((weekday + days_later) % 7) #syntax from Beau, means looking for the correct day
        new_time += f", {days_of_week[weekday_new]}"

    if days_later == 1:
        new_time += " (next day)"

    if days_later > 1:
        new_time += f" ({int(days_later)} days later)"
    
    return new_time
