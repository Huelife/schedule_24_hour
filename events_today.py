#events_today.py: current and future events

import datetime

now = datetime.datetime.now()
datetime.time(now.hour)

hour_12_am = ""
hour_01_am = ""
hour_02_am = ""
hour_03_am = ""
hour_04_am = ""
hour_05_am = ""
hour_06_am = ""
hour_07_am = ""
hour_08_am = ""
hour_09_am = ""
hour_10_am = ""
hour_11_am = ""

hour_12_pm = ""
hour_01_pm = ""
hour_02_pm = ""
hour_03_pm = ""
hour_04_pm = ""
hour_05_pm = ""
hour_06_pm = ""
hour_07_pm = ""
hour_08_pm = ""
hour_09_pm = ""
hour_10_pm = ""
hour_11_pm = ""

#----------------------------------------------

hour_12_am2 = "12am:"
hour_01_am2 = "1am:"
hour_02_am2 = "2am:"
hour_03_am2 = "3am:"
hour_04_am2 = "4am:"
hour_05_am2 = "5am:"
hour_06_am2 = "6am:"
hour_07_am2 = "7am:"
hour_08_am2 = "8am:"
hour_09_am2 = "9am:"
hour_10_am2 = "10am:"
hour_11_am2 = "11am:"

hour_12_pm2 = "12pm:"
hour_01_pm2 = "1pm:"
hour_02_pm2 = "2pm:"
hour_03_pm2 = "3pm:"
hour_04_pm2 = "4pm:"
hour_05_pm2 = "5pm:"
hour_06_pm2 = "6pm:"
hour_07_pm2 = "7pm:"
hour_08_pm2 = "8pm:"
hour_09_pm2 = "9pm:"
hour_10_pm2 = "10pm:"
hour_11_pm2 = "11pm:"

#--------------------------------------------

schedule_event = (hour_12_am,hour_01_am,hour_02_am,hour_03_am,hour_04_am,
                  hour_05_am,hour_06_am,hour_07_am,hour_08_am,hour_09_am,
                  hour_10_am,hour_11_am,hour_12_pm,hour_01_pm,hour_02_pm,
                  hour_03_pm,hour_04_pm,hour_05_pm,hour_06_pm,hour_07_pm,
                  hour_08_pm,hour_09_pm,hour_10_pm,hour_11_pm)

schedule_hr = (hour_12_am2,hour_01_am2,hour_02_am2,hour_03_am2,hour_04_am2,
               hour_05_am2,hour_06_am2,hour_07_am2,hour_08_am2,hour_09_am2,
               hour_10_am2,hour_11_am2,hour_12_pm2,hour_01_pm2,hour_02_pm2,
               hour_03_pm2,hour_04_pm2,hour_05_pm2,hour_06_pm2,hour_07_pm2,
               hour_08_pm2,hour_09_pm2,hour_10_pm2,hour_11_pm2)

x = 24 - now.hour
p = now.hour

check = input("Press 'enter' to check your schedule.")

if check == "":
  for i in range(x):
    print(schedule_hr[p],schedule_event[p])
    p += 1
else:
  print("ERROR!")
