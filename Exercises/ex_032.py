import datetime

year = int(input('Type a year: or 0 for current year: '))
baseYear = 2000

if year == 0:
    year = datetime.date.today().year
else:
    year = year

print('{} Its an bizarre year'.format(year)) if (baseYear + year)%4 == 0 else print('{} its an even year'.format(year))