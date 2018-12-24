from collections import namedtuple, deque
import fileinput
import re
import heapq


def furthest_shortest_path(graph, source):
	result = 0
	visited = set()
	queue = [(0, [source])]

	while queue:
		distance, path = heapq.heappop(queue)

		node = path[-1]

		if node in visited:
			continue

		visited.add(node)

		# For part1
		# result = max(result, distance)

		# For part2
		if distance >= 1000:
			result += 1

		for neighbor in graph.adjacents(node):
			if neighbor in visited:
				continue
			heapq.heappush(queue, (distance + 1, path + [neighbor]))


	return result


class Point(namedtuple('Point', ['x', 'y'])):

	def __add__(self, point):
		return Point(self.x + point.x, self.y + point.y)

SOUTH = Point(0, 1)
NORTH = Point(0, -1)
EAST = Point(1, 0)
WEST = Point(-1, 0)

from_char = {
	'S': SOUTH,
	'N': NORTH,
	'E': EAST,
	'W': WEST
}

class Graph:
	"""Implementation of a not directed graph."""

	def __init__(self):
		self.adj = dict()

	def add_edge(self, p1, p2):
		if not p1 in self.adj:
			self.adj[p1] = set()
		self.adj[p1].add(p2)
		if not p2 in self.adj:
			self.adj[p2] = set()
		self.adj[p2].add(p1)

	def adjacents(self, p1):
		return self.adj[p1]

	def __str__(self):
		return str(self.adj)

	def print(self):
		for k, v in self.adj.items():
			print('%s: %s' % (k, v))


def branch(graph, r, i, last_nodes):
	all_possible_last_nones = set()
	next_char = r[i]
	new_last_nodes = last_nodes.copy()
	while next_char != ')':
		if next_char.isupper():
			temp = set()
			while new_last_nodes:
				last_node = new_last_nodes.pop()
				next_node = last_node + from_char[next_char]
				graph.add_edge(last_node, next_node)
				temp.add(next_node)
			new_last_nodes = temp

		elif next_char == '|':
			all_possible_last_nones.update(new_last_nodes)
			if r[i+1] == ')':
				all_possible_last_nones.update(last_nodes)
				i += 1
				break
			new_last_nodes = last_nodes.copy()

		elif next_char == '(':
			i, new_last_nodes = branch(graph, r, i+1, new_last_nodes)

		i += 1
		next_char = r[i]

	all_possible_last_nones.update(new_last_nodes)
	print(all_possible_last_nones)
	return i, all_possible_last_nones



def run(r):
	graph = Graph()
	root = Point(0, 0)

	next_char = r[0]
	next_node = root + from_char[next_char]

	graph.add_edge(root, next_node)

	last_nodes = set([next_node])
	#print(last_pos)

	next_char = r[1]
	i = 1
	while next_char != '$':
		if next_char.isupper():
			temp = set()
			while last_nodes:
				last_node = last_nodes.pop()
				next_node = last_node + from_char[next_char]
				graph.add_edge(last_node, next_node)
				temp.add(next_node)
			last_nodes = temp

		elif next_char == '(':
			i, last_nodes = branch(graph, r, i+1, last_nodes)

		else:
			raise Exception('Illegal Character \'%s\'' % next_char)
		i += 1
		next_char = r[i]

	
	print("Parse Finished")
	print("Result: %d" % furthest_shortest_path(graph, root))


route = "^N(NW(SE)|ES)$"
route = list(fileinput.input()).pop()
#route = "^WNE$"
#route = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"

m = re.findall('\^(.*?\$)', route.strip())

if m == []:
	print("Parsing error")
	exit()

route = deque(m[0])
print(route)
run(route)



