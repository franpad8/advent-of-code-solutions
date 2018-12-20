
INPUT = list(map(int, list(str(846601))))
scoreboard = [3, 7]
pointer_1 = 0 # pos of first elf
pointer_2 = 1 # pos of second elf

cache = [3, 7]

for _ in range(0, 100000000):
	s = scoreboard[pointer_1] + scoreboard[pointer_2]
	first_digit = s % 10
	second_digit = s // 10
	if second_digit:
		scoreboard.append(second_digit)
		if len(cache) > 5:
			cache.pop(0)
		cache.append(second_digit)
		if cache == INPUT:
			print(len(scoreboard)-6)
			exit(0)


	scoreboard.append(first_digit)
	if len(cache) > 5:
		cache.pop(0)
	cache.append(first_digit)
	if cache == INPUT:
		print(len(scoreboard)-8)
		exit()
	pointer_1 = (pointer_1 + scoreboard[pointer_1] + 1) % len(scoreboard)
	pointer_2 = (pointer_2 + scoreboard[pointer_2] + 1) % len(scoreboard)


print("termino")





#print(scoreboard[846601:846601+10])

