myTime = list(map(int, input("Enter time in hr min : ") .split()))

if((myTime[0] < 7 or myTime[0] > 23) or myTime[1] > 60 or (myTime[2] < 7 or myTime[2] > 23) or myTime[3] > 60):
    print("Invalid time")
else:
  in_time = myTime[0]*60 + myTime[1]
  out_time = myTime[2]*60 + myTime[3]

  total_time =  out_time - in_time

  if(total_time%60 != 0):
    reminder = 1
  else:
    reminder = 0

  if (total_time <= 15):
    tax = 0
  elif (total_time <= 240):
    if (total_time <= 180):
      tax = int(reminder)*10 + int(total_time/60)*10
    else:
      tax = int(reminder)*20 + int(total_time/60)*10
  elif (total_time > 240) and (total_time <= 360):
    tax = int(reminder)*20 + int(total_time/60)*20
  else:
    tax = 200

  print(tax)
