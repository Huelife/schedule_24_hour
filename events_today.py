#events_today.py: Current and future events

import datetime

now = datetime.datetime.now()
datetime.time(now.hour)

#24 variables to edit for events
hour_12_am = "12am: " + ""
hour_01_am = "1am: " + ""
hour_02_am = "2am: " + ""
hour_03_am = "3am: " + ""
hour_04_am = "4am: " + ""
hour_05_am = "5am: " + ""
hour_06_am = "6am: " + ""
hour_07_am = "7am: " + ""
hour_08_am = "8am: " + ""
hour_09_am = "9am: " + ""
hour_10_am = "10am: " + ""
hour_11_am = "11am: " + ""

hour_12_pm = "12pm: " + ""
hour_01_pm = "1pm: " + ""
hour_02_pm = "2pm: " + ""
hour_03_pm = "3pm: " + ""
hour_04_pm = "4pm: " + ""
hour_05_pm = "5pm: " + ""
hour_06_pm = "6pm: " + ""
hour_07_pm = "7pm: " + ""
hour_08_pm = "8pm: " + ""
hour_09_pm = "9pm: " + ""
hour_10_pm = "10pm: " + ""
hour_11_pm = "11pm: " + ""

#------------tuple for event
schedule_event = (hour_12_am,hour_01_am,hour_02_am,hour_03_am,hour_04_am,
                  hour_05_am,hour_06_am,hour_07_am,hour_08_am,hour_09_am,
                  hour_10_am,hour_11_am,hour_12_pm,hour_01_pm,hour_02_pm,
                  hour_03_pm,hour_04_pm,hour_05_pm,hour_06_pm,hour_07_pm,
                  hour_08_pm,hour_09_pm,hour_10_pm,hour_11_pm)

#for loop variables
hr_range = 24 - now.hour
current_hr = now.hour
missed_hr = 0

#user input and printing through for loop generator
check = input("Press 'enter' to check your schedule.")

if check == "":
  for i in range(hr_range):
    print(schedule_event[current_hr])
    current_hr += 1
  print("")
  print("Missed events:")
  for i in range(now.hour):
    print(" {}".format(schedule_event[missed_hr]))
    missed_hr += 1
else:
  print("ERROR!")
