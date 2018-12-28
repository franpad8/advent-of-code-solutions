from re import findall
import fileinput
import heapq

def manhattan_distance(p1, p2):
	(x1, y1, z1), (x2, y2, z2) = p1, p2
	return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

lines = list(fileinput.input())

max_nanobot = (-1, -1, -1)
max_radius = -1
nanobots = dict()

min_x, min_y, min_z = [None] * 3
max_x, max_y, max_z = [None] * 3

graph = dict()


for line in lines:
	x, y, z, r = map(int, findall('-?\d+', line))
	pos = (x, y, z)
	nanobots[pos] = r

	min_x = min(min_x, x) if min_x else x
	min_y = min(min_y, y) if min_y else y
	min_z = min(min_z, z) if min_z else z
	max_x = max(max_x, x) if max_x else x
	max_y = max(max_y, y) if max_y else y
	max_z = max(max_z, z) if max_z else z

	if r > max_radius:
		max_nanobot = pos
		max_radius = r

num_in_range = len(set([p for p in nanobots
					if manhattan_distance(max_nanobot, p) <= max_radius]))


max_cover_coord = max(max(abs(pos[i]) + r for pos, r in nanobots.items()) for i in (0, 1, 2))

print(max_cover_coord)

box_size = 1
while box_size <= max_cover_coord:
	box_size *= 2

# box -> (x0, y0, z0) -> (x1, y1, z1)
initial_box = ((-box_size, -box_size, -box_size),
			   (box_size, box_size, box_size))

def is_intersecting(box, botp, botr):
	d = 0
	for i in (0, 1, 2):
		boxlow, boxhigh = box[0][i], box[1][i] - 1
		d += abs(botp[i] - boxlow) + abs(botp[i] - boxhigh)
		d -= boxhigh - boxlow
	d //= 2
	return d <= botr

def num_intersects(box):
	return sum(1 for botp, botr in nanobots.items()
			   	if is_intersecting(box, botp, botr))


queue = [(-len(nanobots), -2*box_size, 3*box_size, initial_box)]

while queue:

	num_reach, size, dis_to_origin, box = heapq.heappop(queue)
	if size == -1:
		print("Found closest at %s dist %s (%s bots in range)" %
              (str(box[0]), dis_to_origin, -num_reach))
		break
	new_size = size // -2
	for octant in [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
					(1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]:
		newbox0 = tuple(box[0][i] + new_size * octant[i] for i in (0, 1, 2))
		newbox1 = tuple(newbox0[i] + new_size for i in (0, 1, 2))
		newbox = (newbox0, newbox1)
		new_num_reach = num_intersects(newbox)
		heapq.heappush(queue,
						(-new_num_reach, -new_size, manhattan_distance(newbox0, (0, 0, 0)), newbox))





#Part 1
#print(num_in_range)