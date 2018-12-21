import fileinput
import re
from collections import defaultdict


def addr(inst, inp):
	ra, rb, rc = inst[1:]

	if not ra in range(4) or not rb in range(4) or not rc in range(4):
		return False

	va = inp[ra]
	vb = inp[rb]
	vc = va + vb
	result = inp.copy()
	result[rc] = vc

	return result


def addi(inst, inp):
	ra, vb, rc = inst[1:]
	if not ra in range(4) or not rc in range(4):
		return False

	va = inp[ra]
	vc = va + vb

	result = inp.copy()
	result[rc] = vc

	return result

def mulr(inst, inp):
	ra, rb, rc = inst[1:]

	if not ra in range(4) or not rb  in range(4) or rc not in range(4):
		return False

	va = inp[ra]
	vb = inp[rb]
	vc = va * vb
	result = inp.copy()
	result[rc] = vc

	return result

def muli(inst, inp):
	ra, vb, rc = inst[1:]

	if ra not in range(4) or rc not in range(4):
		return False

	va = inp[ra]
	vc = va * vb

	result = inp.copy()
	result[rc] = vc

	return result


def banr(inst, inp):
	ra, rb, rc = inst[1:]

	if ra not in range(4) or rb not in range(4) or rc not in range(4):
		return False

	va = inp[ra]
	vb = inp[rb]
	vc = va & vb
	result = inp.copy()
	result[rc] = vc

	return result


def bani(inst, inp):
	ra, vb, rc = inst[1:]

	if ra not in range(4) or rc not in range(4):
		return False

	va = inp[ra]
	vc = va & vb

	result = inp.copy()
	result[rc] = vc

	return result


def borr(inst, inp):
	ra, rb, rc = inst[1:]

	if ra not in range(4) or rb not in range(4) or rc not in range(4):
		return False

	va = inp[ra]
	vb = inp[rb]
	vc = va | vb
	result = inp.copy()
	result[rc] = vc

	return result


def bori(inst, inp):
	ra, vb, rc = inst[1:]

	if ra not in range(4) or rc not in range(4):
		return False

	va = inp[ra]
	vc = va | vb

	result = inp.copy()
	result[rc] = vc

	return result

def setr(inst, inp):
	ra, _, rc = inst[1:]

	if ra not in range(4) or rc not in range(4):
		return False

	va = inp[ra]
	result = inp.copy()
	result[rc] = va

	return result


def seti(inst, inp):
	va, _, rc = inst[1:]

	if rc not in range(4):
		return False

	result = inp.copy()
	result[rc] = va

	return result


def gtir(inst, inp):
	va, rb, rc = inst[1:]

	if rb not in range(4) or rc not in range(4):
		return False
	vb = inp[rb]

	result = inp.copy()
	result[rc] = 1 if va > vb else 0

	return result

def gtri(inst, inp):
	ra, vb, rc = inst[1:]

	if ra not in range(4) or rc not in range(4):
		return False
	va = inp[ra]

	result = inp.copy()
	result[rc] = 1 if va > vb else 0

	return result

def gtrr(inst, inp):
	ra, rb, rc = inst[1:]

	if ra not in range(4) or rb not in range(4) or rc not in range(4):
		return False

	va = inp[ra]
	vb = inp[rb]

	result = inp.copy()
	result[rc] = 1 if va > vb else 0

	return result

def eqir(inst, inp):
	va, rb, rc = inst[1:]

	if rb not in range(4) or rc not in range(4):
		return False
	vb = inp[rb]

	result = inp.copy()
	result[rc] = 1 if va == vb else 0

	return result

def eqri(inst, inp):
	ra, vb, rc = inst[1:]

	if ra not in range(4) or rc not in range(4):
		return False
	va = inp[ra]

	result = inp.copy()
	result[rc] = 1 if va == vb else 0

	return result

def eqrr(inst, inp):
	ra, rb, rc = inst[1:]

	if not ra in range(4) or not rb in range(4) or not rc in range(4):
		return False

	va = inp[ra]
	vb = inp[rb]

	result = inp.copy()
	result[rc] = 1 if va == vb else 0

	return result

"""

def addr(r, a, b, c): r[c] = r[a] + r[b]
def addi(r, a, b, c): r[c] = r[a] + b
def mulr(r, a, b, c): r[c] = r[a] * r[b]
def muli(r, a, b, c): r[c] = r[a] * b
def banr(r, a, b, c): r[c] = r[a] & r[b]
def bani(r, a, b, c): r[c] = r[a] & b
def borr(r, a, b, c): r[c] = r[a] | r[b]
def bori(r, a, b, c): r[c] = r[a] | b
def setr(r, a, b, c): r[c] = r[a]
def seti(r, a, b, c): r[c] = a
def gtir(r, a, b, c): r[c] = int(a > r[b])
def gtri(r, a, b, c): r[c] = int(r[a] > b)
def gtrr(r, a, b, c): r[c] = int(r[a] > r[b])
def eqir(r, a, b, c): r[c] = int(a == r[b])
def eqri(r, a, b, c): r[c] = int(r[a] == b)
def eqrr(r, a, b, c): r[c] = int(r[a] == r[b])
"""

ops = [
	addr, addi, mulr, muli, banr, bani, borr, bori,
	setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr
]

def parse(line):
    return list(map(int, re.findall(r'\d+', line)))

def discard_opcode(d):
	to_discard = [(op, opcodes.pop()) for op, opcodes in d.items() if len(opcodes)==1]


	for op, opcode in to_discard:
		del d[op]

	for op in d:
		for _, opcode_to_discard in to_discard:
			if opcode_to_discard in d[op]:
				d[op].remove(opcode_to_discard)

	return to_discard


if __name__ == "__main__":
	lines = [l for l in list(fileinput.input()) if l != '\n']

	opcodes = {}

	count = 0
	for line in lines:
		if 'Before' in line:
			before = parse(line)
		elif 'After' in line:
			after = parse(line)
			# count how many examples behave like 3 or more functions
			inner_count = 0
			matched_ops = set()
			opcode = instruction[0]
			for op in ops:
				r = before.copy()
				res = op(instruction, r)
				if res == after:
					if not op.__name__ in opcodes:
						opcodes[op.__name__] = set()
					opcodes[op.__name__].add(opcode)
					inner_count += 1

			if inner_count >= 3:

				count += 1
	        
		else:
			instruction = parse(line)

	map_opcodes = []
	print()
	for _ in range(0, 16):
		map_opcodes += (discard_opcode(opcodes))


	opcodes = dict([
		(5, eqrr), (6, gtri), (12, eqir), (15, gtrr), (9, eqri),
		(7, gtir), (3, setr), (10, bani), (0, banr), (14, seti),
		(8, borr), (11, addr), (1, muli), (13, mulr), (4, addi),
		(2, bori)
	])

	with open('in1.txt', 'r') as f:
		test_program = [list(map(int, re.findall('\d+', l.strip()))) for l in f.readlines()]
		
		registers = [0, 0, 0, 0]
		for instruction in test_program:
			opcode, a, b, c = instruction
			op = opcodes[opcode]
			registers = op(instruction, registers)

		print(registers)




	




