import collections

def print_circle(circle, current_marble_pos):
	result = ""
	for i in range(0..len(circle)):
		if i == current_marble_pos:
			result += "(%d) " % circle[i]
		else:
			result += "%d " % circle[i]
	
	return result


def max_value_from_hash(h):
	return max(h.values())


def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

def insert_nth(d, n, e):
    d.rotate(-n)
    d.appendleft(e)
    d.rotate(n)


last_marble = 72059*100
num_players = 411
circle = collections.deque()
circle.append(0)
current_marble = 0
current_marble_pos = 0
player = 1

points = {}

turn = 0
while current_marble <= last_marble:
	current_marble += 1
	if current_marble % 23 != 0:
		circle.rotate(1)
		circle.appendleft(current_marble)
	else:

		circle.rotate(-7)
		points_won = current_marble + circle.popleft()
		if not player in points:
			points[player] = points_won
		else:
			points[player] += points_won

		circle.rotate(1)

	turn += 1
	player = (turn % num_players) + 1


print(max_value_from_hash(points))
