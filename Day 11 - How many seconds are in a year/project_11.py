days_this_year = int(input("How many days are in this year? "))
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

result_365 = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

result_366 = result_365 + hours_in_day * minutes_in_hour * seconds_in_minute

if days_this_year == 366:
  print("There are", result_366, "seconds in a leap year.")
else:
  print("There are", result_365, "seconds in this year.")