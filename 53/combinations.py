import math

def nCr(n,r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)

def test():
	count = 0
	for i in range(23, 101):
		for j in range(1,i):
			if nCr(i,j) > 1000000:
				count += 1
	return count