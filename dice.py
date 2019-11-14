import random

loop = 0
while loop == 0:
	attacker_drm = 2 #because DE unit
	defender_drm = 0
	move_points = 0
	unit_type = input('Leg unit(l), other, or Air Strike(a)?')
	if unit_type == 'l':
		move_points = 8
	elif unit_type == 'a':
		sorties = input('Number of sorties?')
		attacker_drm -= int(sorties)
		attacker_roll = (random.randint(1, 6)) + attacker_drm
		defender_roll = random.randint(1, 6)
		print(attacker_roll)
		print(defender_roll)
	else:
		move_points = 10
	while move_points > 0:
		print("MP cost: 1 clear, 2 enemy city(factory), +1 attacking unit, +1 river or mountain")
		question = input('Attack or normal movement?')
		if question == 'y':
			move_reduce = input(f'How many movement points this attack(Remaining: {move_points})?')
			move_points -= int(move_reduce)
			print('Attacker first')
			reduced = input('Attacker reduced strength?')
			if reduced == 'y':
				attacker_drm -= 2
			isolated_defender = input('Attacking defender with no eligible retreat hex?')
			if isolated_defender == 'y':
				attacker_drm += 2
			city = input('Attacking city hex or rough terrain?')
			if city == 'y':
				attacker_drm -= 1
			river = input('Attacking across river?')
			if river == 'y':
				attacker_drm -= 1
			air_support = input('Air support?')
			if air_support == 'y':
				attacker_drm += 2
			assault = input('Assault?')
			if assault == 'y':
				number_assault = input('How many(max 3)?')
				if number_assault == 1:
					attacker_drm += 1
				elif number_assault == 2:
					attacker_drm += 2
				else:
					attacker_drm += 3
			print('Now defender')
			reduced = input('Defender reduced strength?')
			if reduced == 'y':
				defender_drm -= 2
			ground_support = input('Ground support(2 in total)?')
			if ground_support == 'y':
				defender_drm += 1

			attacker_roll = (random.randint(1, 6)) + attacker_drm
			defender_roll = random.randint(1, 6) + defender_drm
			print(attacker_roll)
			print(defender_roll)
		else:
			move_reduce = input(f'How many movement points(Remaining: {move_points})?')
			move_points -= int(move_reduce)
	print('Run out of movement points...')
