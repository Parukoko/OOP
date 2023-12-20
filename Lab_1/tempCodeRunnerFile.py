in_time = myTime[0]*60 + myTime[1]
out_time = myTime[2]*60 + myTime[3]

total_time =  out_time - in_time

if (total_time <= 15):
	tax = 0
elif (total_time <= 240):
	tax = int(total_time % 60)*10 + int(total_time/60)*10
elif (total_time > 240) and (total_time <= 360):
	tax = int(total_time % 60)*20 + int(total_time/60)*20
else:
	tax = 200

print(tax)
