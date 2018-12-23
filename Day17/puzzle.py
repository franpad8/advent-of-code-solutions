
import fileinput
from re import findall
from time import sleep


clay = set()
sand = set()
still = set()

to_fall = set()
to_spread = set()


def print_grid():
	for y in range(maxy+2):
		row = str(y)
		for x in range(minx-1, maxx+1):
			if (x,y) in sand:
				row += "|"
			elif (x,y) in still:
				row += "~"
			elif (x,y) in clay:
				row += "#"
			else:
				row += "."
		print(row)

def run():
	to_fall.add((flow_vertically, 500, 0))
	while to_fall or to_spread:

		while to_fall:
			func, x, y= to_fall.pop()
			func(x, y)
			#print(sum(1 for x, y in still | sand
	        #      	if y >= miny and y <= maxy))

		while to_spread:
			func, x, y = to_spread.pop()
			func(x, y)
		
def flow_vertically(x, y):
	y0, y1 = y, y
	while y1 <= maxy and not is_pile(x, y1+1):
		sand.add((x, y1))
		y1 += 1

	if y1 <= maxy:
		sand.add((x,y1))
		to_spread.add((flow_horizontally, x, y1))

def flow_horizontally(x, y):
	x0 = x
	while is_pile(x0, y+1) and not is_clay(x0-1, y):
		x0 -= 1
	x1 = x
	while is_pile(x1, y+1) and not is_clay(x1+1, y):
		x1 += 1

	is_clay0 = is_clay(x0-1, y)
	is_clay1 = is_clay(x1+1, y)

	if is_clay0 and is_clay1:
		for xi in range(x0, x1+1):
			still.add((xi, y))

		to_spread.add((flow_horizontally, x, y-1))

	else:
		for xi in range(x0, x1+1):
			sand.add((xi, y))

		if not is_clay0:
			to_fall.add((flow_vertically, x0, y))
		if not is_clay1:
			to_fall.add((flow_vertically, x1, y))

def is_pile(x, y):
	return (x, y) in clay or (x, y) in still

def is_clay(x, y):
	return (x, y) in clay
			
#print_grid()
#print_grid()


# Read File
lines = list(fileinput.input())


minx, maxx, maxy = 100000, 0, 0
# Parse file
for line in lines:
	x, y = None, None
	
	f, s = line.strip().split(',')
	if 'x' in f:
		x = int(f[2:])
		yini, yend = list(map(int, findall('\d+',s)))
		for y in range(yini, yend+1):
			clay.add((x, y))

		minx = min(minx, x)
		maxx = max(maxx, x)
		maxy = max(maxy, yend+1)

	else:
		y = int(f[2:])
		xini, xend = list(map(int, findall('\d+',s)))
		for x in range(xini, xend+1):
			clay.add((x, y))

		maxy = max(maxy, y)
		minx = min(minx, xini)
		maxx = max(maxx, xend)


maxy = max(y for x, y in clay)
miny = min(y for x, y in clay)


run()

print(sum(1 for x, y in still | sand
            if y >= miny and y <= maxy))

print(sum(1 for x, y in still
            if y >= miny and y <= maxy))





