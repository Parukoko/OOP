def char_count(str):
	return {str[i]: str.count(str[i]) for i in range(0, len(str))}
