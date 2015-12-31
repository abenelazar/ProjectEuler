from numpy import linalg as LA
import numpy as np

def fib(n):
	fib_mat = np.array([[1,1],[1,0]])
	return LA.matrix_power(fib_mat, n)
limit = 4000000
inc = fib(3)
mat = fib(2)
total = 0
while mat.max() < limit:
	for row in mat:
		for num in row:
			if num % 2 == 0:
				total += num
	mat = np.dot(mat, inc)

print total

