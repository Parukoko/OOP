def count_minus(str):
	str = map(int, str.split(' '))
	return sum([1 for i in str if i < 0])

x = list(input("Enter String: "))
print(count_minus(x))
