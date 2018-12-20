
def power(x, y, serial_number=7315):
	rack_id = x + 10
	power_level = rack_id * y + serial_number
	power_level *= rack_id
	hundred_digit = (power_level // 100) % 10

	return hundred_digit - 5

def square_power(x, y, size):
	return sum( grid[(i,j)]
			for i in range(x, x+size)
			for j in range(y, y+size)
	)

def best_square(s):
	squares = {(x,y,s): square_power(x,y,s)
		for x in range(1, 301-s+1)
		for y in range(1, 301-s+1)}

	max_square = max(squares, key=squares.get)
	return max_square, squares[max_square]

def best_square_any_size():
	best = None
	max_power = 0
	for k in range(2, 301):
		current = best_square(k)
		if current[1] > max_power:
			best = current[0]
			max_power = current[1]
			print("Current max is with size %s at position %s" % (k, current[0]))

	return best, max_power

grid = {(x,y): power(x,y) for x in range(1,301) for y in range(1,301)}







if __name__ == '__main__':
	print(best_square_any_size())

