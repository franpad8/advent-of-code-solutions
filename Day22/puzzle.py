
import fileinput
import re
import heapq


# key: 0 -> Rock, 1 -> Wet, 2 -> Narrow
# value: 0 -> Torch, 1 -> climbing gear, 2 -> Neither
ALLOWABLE_TOOLS = {
	0: [0, 1],
	1: [1, 2],
	2: [0, 2]
}


def calculate_erosion_type(x, y):
	global target, depth

	if x == 0 and y == 0 or (x, y) == target:
		geo_index = 0

	elif y == 0:
		geo_index = x * 16807

	elif x == 0:
		geo_index = y * 48271

	else:
		geo_index = erosion_level_grid[(x, y-1)] * erosion_level_grid[(x-1, y)]

	erosion_level = (geo_index + depth) % 20183
	erosion_level_grid[(x, y)] = erosion_level

	erosion_type = erosion_level % 3
	erosion_type_grid[(x, y)] = erosion_type
	return erosion_type


def print_grid(grid):

	for y in range(0, HEIGHT):
		row = ""
		for x in range(0, WIDTH):
			if (x, y) != target:
				row += str(grid[(x,y)]) + " "
			else:
				row += "T "

		print(row)

	print("\n"*5)


def adjacents(x, y):

	offsets = [(0,1), (1,0), (-1,0), (0,-1)]
	return [(x+dx, y+dy) for dx, dy in offsets 
				if x + dx >= 0 and x + dx < WIDTH and
				   y + dy >= 0 and y + dy < HEIGHT]

def find_shortest_path():

	queue = [(0, (0,0), 0)]
	best = dict()
	mini = 1000000000000000
	while queue:
		distance, current, current_tool = heapq.heappop(queue)

		best_key = (current, current_tool)
		if best_key in best and best[best_key] <= distance:
			continue
		best[best_key] = distance
		
		if best_key == (target, 0):
			print(distance)
			break


		x0, y0 = current[0], current[1]
		current_erosion_type = erosion_type_grid[(x0, y0)]
		allowable_tools_in_current = ALLOWABLE_TOOLS[current_erosion_type]

		for i in range(3):
			if i != current_tool and i in allowable_tools_in_current:
				heapq.heappush(queue, ((distance + 7), current, i))

		for adj in adjacents(*current):
			x1, y1 = adj[0], adj[1]

			target_erosion_type = erosion_type_grid[(x1, y1)]
			if current_tool in ALLOWABLE_TOOLS[target_erosion_type]:
				heapq.heappush(queue, ((distance + 1), adj, current_tool))






def move(x0, y0, x1, y1, current_tool):
	current_erosion_type = erosion_type_grid[(x0, y0)]
	target_erosion_type = erosion_type_grid[(x1, y1)]

	allowable_tools_in_current = ALLOWABLE_TOOLS[current_erosion_type]
	allowable_tools_in_target = ALLOWABLE_TOOLS[target_erosion_type]

	for a_tool in allowable_tools_in_target:
		if current_tool == a_tool:
			yield (1, a_tool)
		elif a_tool in allowable_tools_in_current:
			yield (8, a_tool)

	




lines = list(fileinput.input())

target = re.match('^target: (\d+),(\d+)$', lines.pop().strip())
target = (int(target.group(1)), int(target.group(2)))

depth = int(re.match('^depth: (\d+)$', lines.pop().strip()).group(1))

if not target or not depth:
	raise Exception('Parse Error')


for i in range(1, 100):
	HEIGHT = target[1] + i
	WIDTH = target[0] + i

	erosion_level_grid = dict()
	erosion_type_grid = dict()

	risk_level = 0
	for x in range(WIDTH):
		for y in range(HEIGHT):
			risk_level += calculate_erosion_type(x, y)


	print("Target: " + str(target))
	print("Depth: "+ str(depth))
	print("Risk level: " + str(risk_level))

	print(find_shortest_path())
	#print(erosion_level_grid)