import sys

def solve(filename):
	print("Processing %s" % filename)

	with open(filename) as fp:
		previous = None 
		current = None 
		increases = 0
		for line in fp.readlines():
			current = int(line.rstrip())

			if previous:
				if current > previous:
					increases += 1

			print("previous=%s current=%s increases=%s" % (previous, current, increases))
					
			previous = current

	print()

solve(sys.argv[1])
