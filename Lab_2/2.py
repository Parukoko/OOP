def count_char_in_string(x, c):
	return [sum([1 for j in i if j==c]) for i in x]

x = list(map(str, input("Enter strings: ").split(" ")))
c = input("Enter character: ")
d = count_char_in_string(x, c)
print(d)
