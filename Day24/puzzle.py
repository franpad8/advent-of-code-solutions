import fileinput
import re

class Group:

	immune_id = 1
	infection_id = 1

	def __init__(self, army, units, hp, attack_damage,
				 attack_type, weaknesses, immunity,
				 initiative):
		self.army = army
		self.units = units
		self.hp = hp
		self.attack_damage = attack_damage
		self.attack_type = attack_type
		self.weaknesses = weaknesses
		self.immunity = immunity
		self.initiative = initiative

		if army == 'Im':
			self.id = Group.immune_id
			Group.immune_id += 1
		elif army == 'In':
			self.id = Group.infection_id
			Group.infection_id += 1
		else:
			raise Exception('Army has to be either \'Im\' or \'In\'')

	@property
	def effective_power(self):
		return self.units * self.attack_damage
	
	def is_alive(self):
		return self.units > 0

	def __repr__(self):
		army = 'Immune' if self.army == 'Im' else 'Infection'
		return '%s group #%d' % (army, self.id)

	def __str__(self):
		army = 'Immune' if self.army == 'Im' else 'Infection'
		return '%s group #%d' % (army, self.id)


def can_deal_damage(agroup, dgroup):
	return not (agroup.attack_type in dgroup.immunity)

def calc_damage(agroup, dgroup):
	damage = agroup.effective_power
	if agroup.attack_type in dgroup.weaknesses:
		damage *= 2
	return damage

class Battle:

	def __init__(self, groups):
		self.groups = groups

	def is_over(self):
		immunes = any(g.is_alive() for g in self.groups if g.army == "Im")
		infections = any(g.is_alive() for g in self.groups if g.army == "In")
		return not immunes or not infections

	def __choose_target(self, attacking_group, defending_groups):
		target = None
		targets = [(calc_damage(attacking_group, de),
					de.effective_power,
					de.initiative,
					de) 
					for de in defending_groups
						if can_deal_damage(attacking_group, de)]
		if targets:
			target = sorted(targets).pop()[-1]
			defending_groups.remove(target)
		return target

	def __target_selection(self):
		selections = dict()
		groups = sorted(self.groups, 
						key=lambda g: (g.effective_power, g.initiative))

		infections = [g for g in self.groups if g.is_alive() and g.army == 'In']
		immunes = [g for g in self.groups if g.is_alive() and g.army == 'Im']
		while groups:
			attacking_group = groups.pop()
			if attacking_group.army == 'In':
				target = self.__choose_target(attacking_group, immunes)
			else:
				target = self.__choose_target(attacking_group, infections)

			if target:
				selections[attacking_group] = target

		return selections
			

	def __attacking(self, selections):

		queue = sorted(selections, key=lambda x: x.initiative)

		while queue:
			attacker = queue.pop()
			if attacker.units <= 0:
				continue

			defending = selections[attacker]
			damage = calc_damage(attacker, defending)
			units_killed = damage // defending.hp
			if units_killed > defending.units:
				units_killed = defending.units
			defending.units -= units_killed

			#print("Attack: %s to %s with %d units killed" % (attacker, defending, units_killed))


	def __fight(self):
		selections = self.__target_selection()
		self.__attacking(selections)

	def run(self):
		i = 0
		while not self.is_over():
			self.__fight()

		groups_left = [g for g in self.groups if g.is_alive()]
		units_left = sum(map(lambda g: g.units, groups_left))
		winner = groups_left[0].army if groups_left else None
		return winner, units_left




def parse_file():
	lines = list(fileinput.input())
	current_army = ''
	groups = []
	for line in lines:
		line = line.strip()
		if not line:
			continue
		if line == 'Immune System:':
			current_army = 'Im'
		elif line == 'Infection:':
			current_army = 'In'
		else:
			m = re.match('(\d+) units each with (\d+) hit points (\(.*\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)', line)
			weaknesses, immunity = [], []
			if m.group(3):
				weak_immu = m.group(3)
				
				weak = re.search('weak to ([\w,\s]+)[;\)]', weak_immu)
				if weak:
					weaknesses = list(map(lambda x: x.strip(), weak.group(1).split(',')))
				immune = re.search('immune to ([\w,\s]+)[;\)]', weak_immu)
				if immune:
					immunity = list(map(lambda x: x.strip(), immune.group(1).split(',')))

			attack_damage = int(m.group(4))
			groups.append((current_army,
						   int(m.group(1)),
						   int(m.group(2)),
						   attack_damage,
						   m.group(5),
						   weaknesses,
						   immunity,
						   int(m.group(6))
						   )
			)

	return groups

def get_groups(pairs, immune_boost=0):
	groups = []
	for p in pairs:
		new_group = Group(*p)
		new_group.attack_damage += immune_boost if p[0] == 'Im' else 0
		groups.append(new_group)

	return groups



if __name__ == '__main__':
	pairs = parse_file()


	#part1
	#winner, remaining_units = Battle(get_groups(pairs)).run()
	#print(winner, remaining_units)
	
	#part2
	boost = 35
	while True:
		winner, remaining_units = Battle(get_groups(pairs, boost)).run()
		if winner == 'Im':
			print(winner, remaining_units)
			break
		print(boost, winner, remaining_units)
		boost += 1
			



				





