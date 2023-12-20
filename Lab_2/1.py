a = list(map(int, input("Enter number : ") .split(" ")))
a.sort()
if a[0] == 0:
	a[0] = a[1]
	a[1] = 0
for i in range(len(a)):
	print(a[i], end='')
