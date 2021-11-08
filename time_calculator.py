def add_time(start, duration, day=None):
    new_time = None

    hr, am_pm = start.split()
    hr, min = start.split(":")
    min = min.split()[0]
    dur_hr, dur_min = duration.split(":")
    hr = int(hr)
    min = int(min)
    dur_hr = int(dur_hr)
    dur_min = int(dur_min)
    weekday = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if (am_pm == "PM"):
        hr += 12
    else:
        pass
    new_hr = hr + dur_hr
    new_min = min + dur_min
    while (new_min > 59):
        new_hr += 1
        new_min -= 60

    days_passed = 0
    while (new_hr > 23):
        days_passed += 1
        new_hr -= 24

    print(new_hr)

    if(new_hr > 11):
        am_pm = "PM"
    else:
        am_pm = "AM"

    new_hr = new_hr % 12

    if (new_hr == 0):
        new_hr = 12
    else:
        pass

    if (new_min < 10):
        new_min = "0" + str(new_min)
    else:
        pass

    new_time = str(new_hr) + ":" + str(new_min) + " " + am_pm

    if (day):
        new_day = weekday[(weekday.index(day.lower()) + days_passed) % 7].capitalize()
        new_time += ", " + new_day
    if (days_passed == 1):
        new_time += " (next day)"
    if (days_passed > 1):
        new_time += " (" + str(days_passed) + " days later)"

    return new_time
