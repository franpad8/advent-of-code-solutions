import re

points = []
velocity = []
with open('in.txt', "r") as file:
	lines = file.readlines()
	for line in lines:
		x,y,vx,vy = list(map(int, re.findall('-?\d+', line.strip())))
		points.append((x,y,))
		velocity.append((vx,vy,))


def update(points):
	for i in range(0, len(points)):
		points[i] = (points[i][0]+velocity[i][0], points[i][1]+velocity[i][1])
		


def print_board(points):
	maxx = max([x[0] for x in points])
	maxy = max([x[1] for x in points])
	minx = min([x[0] for x in points])
	miny = min([x[1] for x in points])
	dx = maxx - minx
	dy = maxy - miny
	#return "%d , %d" % (dx, dy)
	rows = []
	for i in range(0, maxy+100):
		row = ""
		for j in range(0, maxx+100):
			if (j,i) in points:
				row += "#"
			else:
				row += "."
		rows.append(row)

	return "\n".join(rows)


i = 1
while True:
	update(points)
	if abs(i - 10515) == 0 :
		print(print_board(points))

	i += 1

