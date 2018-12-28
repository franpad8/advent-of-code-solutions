import fileinput
import re


def manhattan(p1, p2):
	return sum(abs(p1i - p2i) for p1i, p2i in zip(p1, p2))

def are_connected(p1, p2):
	return manhattan(p1, p2) <= 3

def find_number_constelations(points):
	num_constelations = 0
	while points:
		visited = set()
		p0 = points[0]
		stack = [p0]
		while stack:
			current = stack.pop()
			if current in visited:
				continue

			visited.add(current)
			points.remove(current)
			connected = [p for p in points if are_connected(current, p)]
			for c in connected:
				if not c in visited:
					stack.append(c)

		num_constelations += 1

	return num_constelations


def main():
	lines = list(fileinput.input())
	points = [tuple(map(int, re.findall('-?\d+', line.strip())))
			  for line in lines]

	n_const = find_number_constelations(points.copy())

	print(n_const)


if __name__ == '__main__':
	main()