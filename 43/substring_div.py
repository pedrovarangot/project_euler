from itertools import permutations

primes = {2:2,3:3,4:5,5:7,6:11,7:13,8:17}

def test(n=9):
	numstr = ''
	for i in range(n+1):
		numstr += str(i)
	print(numstr)
	nums_list = [''.join(d) for d in permutations(numstr, n+1)]
	for pandigital in nums_list:
		doesit = True
		for i in range(2,n):
			doesit = (int(pandigital[i-1:i+2]) % primes[i]) == 0
			if not doesit:
				break
		if doesit:
			yield int(pandigital)