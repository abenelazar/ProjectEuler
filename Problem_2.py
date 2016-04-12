from numpy.linalg import matrix_power
import numpy as np

limit = 4000000

def fib(n):
	fib_mat = np.array([[1,1],[1,0]])
	return matrix_power(fib_mat, n)


def solution():
	cumulative_total = 0
	inc = fib(3) # increment matrix for fib_mat
	fib_mat = fib(2) # gives fib 1, 2, 3 
	
	while fib_mat.max() < limit:
		for row in fib_mat:
			for entry in row:
				if entry % 2 == 0: # only evens
					cumulative_total += entry
		fib_mat = np.dot(fib_mat, inc) # next matrix with entries i-1, i, i+1
	return cumulative_total

print solution() # ans

