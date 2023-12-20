def delete_minus(lst_of_lst):
	result = []
	for sublist in lst_of_lst:
		result.append([num for num in sublist if num >= 0])
	return result

x = list(input("Enter number: "))
print(delete_minus(x))
