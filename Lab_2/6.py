def add2list(lst1,lst2):
	return [lst1[i] + lst2[i] for i in range(len(lst1))]

x = list(map(int, input("Enter numbers: ").split(" ")))
y = list(map(int, input("Enter numbers: ").split(" ")))

print(add2list(x,y))
