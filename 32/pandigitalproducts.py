from itertools import permutations	

nums_list = [''.join(d) for d in permutations('123456789', 9)]

def test():
	for numstr in nums_list:
		for i in range(1, 7+1):
			for j in range(i+1, 8+1):
				a = int(numstr[:i])
				b = int(numstr[i:j])
				c = int(numstr[j:])

				if a * b == c:
					yield c

def test2():
	for numstr in nums_list:
		for i in range(1, 7+1):
			for j in range(i+1, 8+1):
				if i > 9 - j or j-i > 9-j:
					continue
				a = int(numstr[:i])
				b = int(numstr[i:j])
				c = int(numstr[j:])
				if a * b == c:
					yield c
