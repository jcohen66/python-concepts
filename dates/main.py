from datetime import date, datetime, time

today = date.today()
print(f"today is: {today}")
print(f"day: {today.day}")
print(f"month: {today.month}")
print(f"year: {today.year}")

print(today.strftime("%A, %dth of %B %Y"))
print(today.strftime("%a, %dth of %b %y"))

next_year = today.replace(year=today.year + 1)
print(next_year)

difference = abs(next_year - today)
print(f"only {difference.days} days until next year")

nikolaTesla = date(1856, 7, 10)
nikolaTesla = date.fromisoformat("1856-07-10")
print(f"Nikola Tesla was born on: {nikolaTesla}")
print(nikolaTesla.weekday())


now = datetime.now()
print(f"The time right now is: {now}")
print(
    f"Its the {now.minute}th minute of the {now.hour}nd hour of the {now.day}th day of the {now.month}nd month"
)

chernobyl = datetime.fromisoformat("1986-04-26 01:23:40:000+04:00")
print(f"the nuclear disaster in Chernobyl occured on: {chernobyl}")
print(
    chernobyl.strftime(
        "The Chernobyl disaster occurred on %A %B %dth, %Y at %X MSD(%Z)"
    )
)
print(f"MSD is actually: {chernobyl.tzinfo}")

my_time = time(15, 33, 8)
my_time = time.fromisoformat("15:33:08-07:00")
print(my_time)
print(my_time.strftime("%I:%M %p"))

my_date = date(2022, 5, 22)
my_bday = datetime.combine(my_date, my_time)
print(my_time)
