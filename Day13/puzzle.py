from time import sleep


class CollisionError(Exception):
	def __init__(self, pos, *args, **kwargs):
		super(CollisionError).__init__(*args, **kwargs)
		self.pos = pos

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


DIRECTION = {
	'v': DOWN,
	'^': UP,
	'<': LEFT,
	'>': RIGHT
}

DIRECTION_REVERSE = {
	DOWN: 'v',
	UP: '^',
	LEFT: '<',
	RIGHT: '>',
}

INTER_TURNS = {
	(DOWN, LEFT): RIGHT,
	(DOWN, RIGHT): LEFT,
	(UP, LEFT): LEFT,
	(UP, RIGHT): RIGHT,
	(LEFT, LEFT): DOWN,
	(LEFT, RIGHT): UP,
	(RIGHT, LEFT): UP,
	(RIGHT, RIGHT): DOWN,
}

CURVE_TURNS = {
	(DOWN, '/'): LEFT,
	(DOWN, "\\"): RIGHT,
	(UP, '/'): RIGHT,
	(UP, "\\"): LEFT,
	(LEFT, '/'): DOWN,
	(LEFT, "\\"): UP,
	(RIGHT, '/'): UP,
	(RIGHT, "\\"): DOWN,
}

OVER = {
	DOWN: '|',
	UP: '|',
	LEFT: '-',
	RIGHT: '-'
}


OPPOSITE = {
	(0, -1): (0, 1),
	(0, 1): (0, -1),
	(-1, 0): (1, 0),
	RIGHT: LEFT
}


class Cart(object):
	def __init__(self, pos, direction):
		self.pos = pos
		self.dir = direction
		self.intersec_queue = [LEFT, None, RIGHT]
		self.over = OVER[self.dir]

	def __str__(self):
		return "%s" % (DIRECTION_REVERSE[self.dir])

	def __repr__(self):
		return "%s at %s" % (self.dir, self.pos)

	def update_dir_after_intersect(self):
		next_turn = self.intersec_queue.pop(0)
		if next_turn:
			self.dir = INTER_TURNS[(self.dir, next_turn)]

		self.intersec_queue.append(next_turn)

	def move(self):
		next_pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
		track[self.pos] = self.over
		self.over = track[next_pos]
		self.pos = next_pos

		#Check for collisions
		if type(self.over) == type(self):

			track[next_pos] = self.over.over

			raise CollisionError(self.pos)

		if self.over in ['/', '\\']:
			self.dir = CURVE_TURNS[(self.dir, self.over)]

		elif self.over == '+':
			self.update_dir_after_intersect()

		track[next_pos] = self



def print_track(track):

	for y in range(0, height):
		row = ""
		for x in range(0, width):
			row += track[(x,y)] + " "

		print(row)

	print("\n"*5)

def get_carts(track):
	return [Cart(pos, DIRECTION[track[pos]]) for pos in track if track[pos] in DIRECTION]

def update():
	for cart in sorted(carts, key=lambda c: c.pos):
		cart.move()

def handle_collision(pos):
	global carts
	carts = [c for c in carts if c.pos != pos]

	print(carts)

def is_over():
	if len(carts) == 1:
		print("The last cart ended up at %s, %s" % carts[0].pos)
		return True
	return False

def main_loop():
	while True:
		try:
			update()
		except CollisionError as e:
			
			handle_collision(e.pos)

		if is_over():
			break
		#print_track(track)
		#sleep(0.5)


with open('in.txt', 'r') as f:
	lines = f.readlines()
	height = len(lines)
	width = len(lines[0])
	track = {(x,y): lines[y][x] for y in range(0, height) for x in range(0, width)}
	print(height)
	print(width)
	#print_track(track)
	carts = get_carts(track)

	main_loop()