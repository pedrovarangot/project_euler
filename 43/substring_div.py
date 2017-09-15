from itertools import permutations

A050278_list = [''.join(d) for d in permutations('0123456789', 10) if d[0] != '0'] # Chai Wah Wu, May 25 2015

primes = {2:2,3:3,4:5,5:7,6:11,7:13,8:17}

def test(n=9):
	for pandigital in A050278_list:
		doesit = True
		for i in range(2,8+1):
			doesit = (int(pandigital[i-1:i+2]) % primes[i]) == 0
			if not doesit:
				break
		if doesit:
			yield int(pandigital)