
import math

def is_square(n):
	nsqrt = math.sqrt(n)
	return nsqrt == math.ceil(nsqrt), int(nsqrt)

def discriminant(a, b, c):
	return b**2 - 4*a*c

def isqrt(n):

	x = n
	y = (2 ** ((n.bit_length()+1) // 2)) - 1

	while y < x:
		x = y
		y = (x + n // x) // 2
	return x

def is_square_2(n):
	MAXF = 256

	if n < MAXF:
		return is_square(n)
	else:
		sqrtn = isqrt(n)
		return sqrtn**2 == n, sqrtn

# 2Tn = n**2 + n
# 2Pn = 3n**2 - n
# Hn = 2n**2 - n

def is_triangle(n):
	sqres = is_square(discriminant(1, 1, -n * 2))
	return solves_cuadratic_in_ints(sqres, 1, 1)

def is_pentagonal(n):
	sqres = is_square(discriminant(3, -1, -n * 2))
	return solves_cuadratic_in_ints(sqres, -1, 3)

def is_hexagonal(n):
	sqres = is_square(discriminant(2, -1, -n))
	return solves_cuadratic_in_ints(sqres, -1, 2)

def solves_cuadratic_in_ints(sqres, b, a):
	if sqres[0]:
		if (-b + sqres[1]) % (2*a) == 0 and -b + sqres[1] > 0:
			return True
		if (-b - sqres[1]) % (2*a) == 0 and -b - sqres[1] > 0:
			return True

	return False

def test():
	n, torp, _ = [int(n) for n in input().strip().split()]
	if torp == 3:
		for i in range(1, n):
			num = (i*(3*i-1)) // 2
			if num > n:
				break
			if is_triangle(num):
				print(num)
	else:
		for i in range(1, n):
			num = (i*(2*i-1))
			if num > n:
				break
			if is_pentagonal(num):
				print(num)

