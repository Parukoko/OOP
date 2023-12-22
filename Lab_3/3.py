def is_plusone_dictionary(d):
	for k, v in d.items():
		if v != k + 1:
			return False
	return True

example_dict = {1:2, 3:4, 5:6, 7:8}
result = is_plusone_dictionary(example_dict)
print(result)
