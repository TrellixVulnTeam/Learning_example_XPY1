import datetime
import pytz

today = datetime.date.today()
print(today)

birthday = datetime.date(1988,6,18)
print(birthday)

divy_birt = datetime.date(1990,9,14)
div_days_since = (today - divy_birt).days
print(div_days_since)

days_since_birth = (today - birthday).days
print(days_since_birth)

tdelta = datetime.timedelta(days=10)
print(today+tdelta)
# Add 10 days to current
print(datetime.datetime.now() + tdelta)

print(today.day)
# monday = 0
print(today.weekday())

# datetime.time(h, m, s, ms)
print(datetime.time(7,2,20,200))

# datetime.date(Y,M,D)
print(datetime.date(2020,5,12))

# datetime.datetime(Y,M,D, h, m, s, ms)
print(datetime.datetime(2020,5,12,19,44,23,200))

# Add 10 hours to current
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)


datetime_today = datetime.datetime.now(tz=pytz.UTC)
print(datetime_today)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/pacific'))
print(datetime_pacific)

