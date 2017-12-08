def ndigits(n):
	return len(str(n))

def test():
	for i in range(1,1000):
		for j in range(1,1000):
			if ndigits(i**j) == j:
				yield i**j
