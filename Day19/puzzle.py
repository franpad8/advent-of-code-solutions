import fileinput
from time import sleep



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



lines = list(fileinput.input())

r_bound = int(lines.pop(0)[4])

registers = [0, 1, 10551367, 3, 10551367, 10551367]

instr_pointer = 4

instructions = [line.strip().split(' ') for line in lines]

n = 10551367
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)



print(r_bound)
print(instructions)
print(registers)
while instr_pointer < len(instructions):
	registers[r_bound] = instr_pointer
	ins = instructions[instr_pointer]
	print("Instruction: %s" % ins)
	print("instr_pointer before %d" % instr_pointer)
	exec('%s(registers, %s, %s, %s)' % (ins[0], ins[1], ins[2], ins[3]))
	instr_pointer = registers[r_bound] +1
	print("instr_pointer after %d" % instr_pointer)
	print(registers)
	sleep(1)
	print()

print(registers)

total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)

