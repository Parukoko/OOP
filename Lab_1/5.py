def isPalindrome(self):
	for i in range(0, int(len(self)/2)):
		if self[i] != self[len(self)- i-1]:
			return False
	return True

palindrome = []
for a in range(100, 999):
	for b in range(100, 999):
		n = a * b
		if (isPalindrome(str(n))):
			palindrome.append(int(n))
			max(palindrome)
print (max(palindrome))

