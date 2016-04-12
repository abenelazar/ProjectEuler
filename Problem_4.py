from numpy.linalg import matrix_power
import numpy as np


def is_palindrome(n):
	n = str(n)
	for c in range(len(n)/2):
		if n[len(n)-c-1] != n[c]:
			return False
	return True


def solution():
	num1 = 999
	num2 = 999
	while True:
		while num2 != num1-1:
			if is_palindrome(num1*num2):
				return num1, num2, num2*num1
			print num1, num2
			num2 -= 1
		num1 -= 1
		num2 = 999



print solution()