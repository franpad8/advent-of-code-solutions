import fileinput


HEIGHT = 50
WIDTH = 50


def print_grid():
	for x in range(0, HEIGHT):
		row = ""
		for y in range(0, WIDTH):
			row += grid[x][y]
		print(row)

def add_points(p1, p2):
	return (p1[0] + p2[0], p1[1] + p2[1])

def adjacents(x, y):
	ds = [(x ,y) for x in range(-1,2) for y in range(-1,2) if (x, y) != (0,0)]
	ds = [add_points((x, y), (dx, dy)) for dx, dy in ds 
										if x + dx < 50 and
										x + dx >= 0 and
										y + dy < 50 and
										y + dy >= 0]

	return [grid[x1][y1] for x1, y1 in ds]


def will_remain_lumberyard(x, y):
	found_lumberyard = False
	found_tree = False

	for elem in adjacents(x,y):
		if elem == '|':
			found_tree = True
		elif elem == '#':
			found_lumberyard = True

		if found_lumberyard and found_tree:
			return True

	return False


def will_become_lumberyard(x,y):
	return len([e for e in adjacents(x,y) if e == '#']) >= 3

def will_become_tree(x,y):

	return len([e for e in adjacents(x,y) if e == '|']) >= 3


def get_changes():
	global num_lumberyards, num_trees
	changes = dict()
	for x in range(0, HEIGHT):
		for y in range(0, WIDTH):
			if grid[x][y] == '#' and not will_remain_lumberyard(x, y):
				changes[(x,y)] = '.'
				num_lumberyards -= 1
			elif grid[x][y] == '|' and  will_become_lumberyard(x, y):
				changes[(x,y)] = '#'
				num_trees -= 1
				num_lumberyards += 1
			elif grid[x][y] == '.' and  will_become_tree(x, y):
				changes[(x,y)] = '|'
				num_trees += 1


	return changes

def apply_changes(changes):
	for pos, symbol in changes.items():
		grid[pos[0]][pos[1]] = symbol

def get_result():
	num_t = 0
	num_l = 0
	for x in range(HEIGHT):
		for y in range(WIDTH):
			if grid[x][y] == '|':
				num_t += 1
			elif grid[x][y] == '#':
				num_l += 1

	return num_t, num_l

def run():
	for i in range(1, 1000000001):	
		apply_changes(get_changes())
		num_t, num_l = get_result()
		print(str(i) + " " + str(num_t*num_l))

	return num_trees * num_lumberyards

	



lines = list(fileinput.input())

grid = [list(line.strip()) for line in lines]


num_trees, num_lumberyards = get_result()

result = run()
print_grid()
print(result)





