import datetime

import events.txt

now = datetime.datetime.now()
datetime.time(now.hour)

now_hr = now.hour
x = 24+now_hr
p = now.hour

check = input("Press 'enter' to check your schedule.")

if check == "":
  for i in range(x):
    print(schedule_hr[p],schedule_event[p])
    p += 1
  #check now hr
  #import events for this hr and rest of day
  #print("")
else:
  print("ERROR!")
