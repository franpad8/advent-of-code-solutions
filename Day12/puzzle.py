import re

def next_generation(state, rules):
	new_state = list(state)
	sum_pos = 0

	for i in range(0, len(state)-2):
		if i< 2:
			pot = ".." + state[i:i+3]
		else:
			pot = state[i-2:i+3]

		if pot in rules:
			new_state[i] = rules[pot]
			sum_pos += i-2 if new_state[i] == '#' else 0
		else:
			new_state[i] = "."

	return "".join(new_state), sum_pos
	
#with open('in.txt', 'r') as f:
with open('in.txt', 'r') as f:
	lines = f.readlines()
	initial_state = ".." + lines[0][15:].strip() + "."*40000
	rules = dict([tuple(s.strip().split(' => ')) for s in lines[2:]])

	print("0: " + initial_state)

	state = initial_state
	for i in range(1, 40000):
		state, sum_pos = next_generation(state, rules)
		print(i)
		print([i-x[0] for x in enumerate(state, -2) if x[1] == '#'])
		#print("%1d: %d  -> %.5f" % (i, sum_pos, i/sum_pos))

	# I notice there was a convergence in the difference between iteration and each positions where there are plants
	l = [26, 22, 15, 9, 5, -5, -9, -15, -19, -23, -28, -36, -42, -48, -54, -60, -64, -68, -72, -76, -80, -86, -90, -94, -99]
	return sum([50000000000 - x for x in l])

