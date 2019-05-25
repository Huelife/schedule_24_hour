#events_today.py: Current and future events

import datetime

now = datetime.datetime.now()
datetime.time(now.hour)

#24 variables to edit for events
hr_12_am = "12am: " + ""
hr_01_am = "1am: " + ""
hr_02_am = "2am: " + ""
hr_03_am = "3am: " + ""
hr_04_am = "4am: " + ""
hr_05_am = "5am: " + ""
hr_06_am = "6am: " + ""
hr_07_am = "7am: " + ""
hr_08_am = "8am: " + ""
hr_09_am = "9am: " + ""
hr_10_am = "10am: " + ""
hr_11_am = "11am: " + ""

hr_12_pm = "12pm: " + ""
hr_01_pm = "1pm: " + ""
hr_02_pm = "2pm: " + ""
hr_03_pm = "3pm: " + ""
hr_04_pm = "4pm: " + ""
hr_05_pm = "5pm: " + ""
hr_06_pm = "6pm: " + ""
hr_07_pm = "7pm: " + ""
hr_08_pm = "8pm: " + ""
hr_09_pm = "9pm: " + ""
hr_10_pm = "10pm: " + ""
hr_11_pm = "11pm: " + ""

#------------tuple for event
schedule_event = (hr_12_am,hr_01_am,hr_02_am,hr_03_am,hr_04_am,
                  hr_05_am,hr_06_am,hr_07_am,hr_08_am,hr_09_am,
                  hr_10_am,hr_11_am,hr_12_pm,hr_01_pm,hr_02_pm,
                  hr_03_pm,hr_04_pm,hr_05_pm,hr_06_pm,hr_07_pm,
                  hr_08_pm,hr_09_pm,hr_10_pm,hr_11_pm)

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
