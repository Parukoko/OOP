a = input("Enter string: ")
count_low = 0
count_high = 0
for i in a:
	if i > "a" and i < "z":
		count_low+=1
	if i > "A" and i < "Z":
		count_high+=1
print("Low: " ,count_low)
print("High: " ,count_high)
