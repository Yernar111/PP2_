import datetime

x=datetime.datetime(int(input("Year: ")),int(input("Month: ")),int(input("Day: ")),int(input("Hour: ")),int(input("Minute: ")),int(input("Second: ")))

y=datetime.datetime(int(input("Year: ")),int(input("Month: ")),int(input("Day: ")),int(input("Hour: ")),int(input("Minute: ")),int(input("Second: ")))

a=x.second+x.minute*60+x.hour*60*60+x.day*60*60*24+x.month*60*60*24*31+x.year*60*60*24*31*365

b=y.second+y.minute*60+y.hour*60*60+y.day*60*60*24+y.month*60*60*24*31+y.year*60*60*24*31*365

print(a-b)