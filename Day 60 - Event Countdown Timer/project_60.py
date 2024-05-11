import datetime

print("Event Countdown Timer")
print()
today = datetime.date.today()
event_name = input("What is the name of the event? ")
event_year = int(input("What year is the event? "))
event_month = int(input("What month is the event? "))
event_day = int(input("What day is the event? "))
event_date = datetime.date(event_year, event_month, event_day)

difference = event_date - today
difference = abs(difference.days)

if today == event_date:
  print(f"🎉🎉 {event_name} is today! 🎉🎉")
elif today > event_date:
  print(f"😢😢 {event_name} was {difference} days ago. 😢😢")
else:
  print(f"😊😊 {event_name} is in {difference} days. 😊😊")
