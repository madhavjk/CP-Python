

def isPalindrome(s):
	return s == s[::-1]



s = input()
ans = isPalindrome(s)

if ans:
	print("S is a palindrome")
else:
	print("S is not a palindrome")
