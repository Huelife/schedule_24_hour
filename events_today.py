import datetime

now = datetime.datetime.now()
datetime.time(now.hour)
now_hr = now.hour

check = input("Press 'enter' to check your schedule.")

if check == "":
  #check now hr
  #import events for this hr and rest of day
  #print("")
else:
  print("ERROR!")
