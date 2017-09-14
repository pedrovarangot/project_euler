import math

def is_square(n):
	nsqrt = math.sqrt(n)
	return nsqrt == math.ceil(nsqrt), int(nsqrt)

maxperimeter = 1
maxsides = set()

def test():
	global maxsides, maxperimeter

	for perimeter in range(2,1000+1, 2):
		sides = set()
		for side1 in range(1, perimeter):
			for side2 in range(1, perimeter - side1 +1):
				squaredata = is_square(side1**2 + side2**2)
				if squaredata[0] and (side1 + side2 + squaredata[1] == perimeter):
					print(side1, side2, squaredata[1], perimeter)
					sides.add(frozenset([side1, side2, squaredata[1]]))
					if len(sides) > len(maxsides):
						maxsides = sides
						maxperimeter = perimeter

