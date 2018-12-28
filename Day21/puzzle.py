from time import sleep
def main():
	#r = [int('101101001010101110010010', 2), 0, 0, 0, 0, 0]
	r = [0, 0, 0, 0, 0, 0]
	count = 0
	i = 1
	maxi = 999999999999999
	repeat = 0
	seen = set()
	cs = set()
	prev = 0
	while True:
		r[2] = r[4] | int('10000000000000000', 2)
		if r[2] in seen:
			exit()
		seen.add(r[2])
		r[4] = int('10111011110000001011101', 2)
		

		while True:
			r[1] = r[2] & int('11111111', 2)
		  	r[4] = r[4] + r[1]
		  	r[4] = r[4] & int('111111111111111111111111', 2)
		  	r[4] = r[4] * 65899
			r[4] = r[4] & int('111111111111111111111111', 2)

			#print([bin(e) for e in r])
		


			if 256 > r[2]:
				if r[4] not in cs:
					print(r[4])
				cs.add(r[4])

				if r[4] == r[0]:
					print(r)
					exit(0)
				else: 
					break
			else:
				r[2] = r[2] // 256

			
			count += 1





if __name__ == '__main__':
	main()