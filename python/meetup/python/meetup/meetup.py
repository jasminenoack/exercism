from datetime import date, timedelta

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

def find_day_of_week(date, day):
    current_day, target_day = date.weekday(), days.index(day)

    if current_day < target_day:
        date += timedelta(target_day - current_day)
    elif target_day < current_day:
        date += timedelta(7 - current_day + target_day)
    return date

def increase_day(date, week):
    current_day = date.day
    if week == "teenth":
        while current_day < 13:
            current_day += 7
    elif week[0].isdigit():
        current_day += 7 * (int(week[0]) - 1)
    elif week == "last":
        while current_day < 25:
            current_day += 7

    date += timedelta(current_day - date.day)
    return date

def meetup_day(year, month, day, week):
    meetup_date = date(year, month, 1)
    meetup_date = find_day_of_week(meetup_date, day)
    meetup_date = increase_day(meetup_date, week)

    if meetup_date.month != month:
        raise Exception

    return meetup_date