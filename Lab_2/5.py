def only_english(string1):
	return ''.join([char for char in string1 if char.isalpha() and not char.isnumeric()])

x = list(input("Enter String: "))
print(only_english(x))
