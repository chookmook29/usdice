import random

loop = 0
while loop == 0:
	attacker_drm = 0
	defender_drm = 0
	move_points = 0
	unit_type = input('Leg unit(l), mobile(m), or Air Strike(a)?')
	if unit_type == 'l':
		move_points = 8
	elif unit_type == 'a':
		sorties = input('Number of sorties?')
		attacker_drm -= int(sorties)
		attacker_roll = (random.randint(1, 6)) + attacker_drm
		defender_roll = random.randint(1, 6)
		print(attacker_roll)
		print(defender_roll)
	elif unit_type == 'm':
		move_points = 10
	while move_points > 0:
		print("MP cost: 1 clear, 2 enemy city(factory), +1 attacking unit, +1 river or mountain")
		question = input('Attack or normal movement?')
		if question == 'y':
			move_reduce = input(f'How many movement points this attack(Remaining: {move_points})?')
			move_points -= int(move_reduce)
			print('Attacker first')
			germ = input('German unit?')
			if germ == 'y':
				attacker_drm += 2
			elite = input('Elite unit(star symbol)?')
			if elite == 'y':
				attacker_drm += 1
			reduced = input('Reduced strength?')
			if reduced == 'y':
				attacker_drm -= 2
			low = input('Low supply?')
			if low == 'y':
				attacker_drm -= 2
			shock = input('Shock unit in fair weather?')
			if shock == 'y':
				attacker_drm += 1
			tank_fair = input('Tank unit in fair weather?')
			if tank_fair == 'y':
				attacker_drm += 2
			tank_poor = input('Tank unit in poor weather?')
			if tank_poor == 'y':
				attacker_drm += 1
			poor = input('Attacking in poor weather?')
			if poor == 'y':
				attacker_drm -= 2
			isolated_defender = input('Attacking isolated defender?')
			if isolated_defender == 'y':
				attacker_drm += 2
			strait = input('Attacking across a strait hex side?')
			if strait == 'y':
				attacker_drm -= 2
			city = input('Attacking city hex or rough terrain?')
			if city == 'y':
				attacker_drm -= 1
			river = input('Attacking across river?')
			if river == 'y':
				attacker_drm -= 1
			air_support = input('Air support in fair weather?')
			if air_support == 'y':
				attacker_drm += 2
			air_support_poor = input('Air support in poor weather?')
			if air_support_poor == 'y':
				attacker_drm += 1
			assault = input('Assault in fair/poor weather(+2 for each tank or shock) max 2 extra units?')
			if assault == 'y':
				number_assault = input('How many points?')
				if number_assault == 1:
					attacker_drm += 1
				elif number_assault == 2:
					attacker_drm += 2
				elif number_assault == 3:
					attacker_drm += 3
				else:
					attacker_drm += 4
			assault_s = input('Assault in severe weather max 2 extra units?')
			if assault_s == 'y':
				number_assault = input('How many points(max 2)?')
				if number_assault == 1:
					attacker_drm += 1
				else:
					attacker_drm += 2
			events = input('Tanks event(except shock unit), Heavy Arty(+2) or Ground Support(+1)?')
			if events == 'y':
				number_events = input('How many points?')
				if number_events == 1:
					attacker_drm += 1
				elif number_events == 2:
					attacker_drm += 2
				elif number_events == 3:
					attacker_drm += 3
			print('Now defender')
			germ = input('German unit?')
			if germ == 'y':
				defender_drm += 2
			elite = input('Elite unit(star symbol)?')
			if elite == 'y':
				defender_drm += 1
			reduced = input('Reduced strength?')
			if reduced == 'y':
				defender_drm -= 2
			low = input('Low supply?')
			if low == 'y':
				defender_drm -= 2
			shock = input('Shock unit in fair weather?')
			if shock == 'y':
				defender_drm += 1
			tank_fair = input('Tank unit in fair weather?')
			if tank_fair == 'y':
				defender_drm += 2
			tank_poor = input('Tank unit in poor weather?')
			if tank_poor == 'y':
				defender_drm += 1
			air_support = input('Air support in fair weather?')
			if air_support == 'y':
				defender_drm += 2
			air_support_poor = input('Air support in poor weather?')
			if air_support_poor == 'y':
				defender_drm += 1
			events = input('Tanks event(except shock unit), Heavy Arty(+2) or Ground Support(+1)?')
			if events == 'y':
				number_events = input('How many points?')
				if number_events == 1:
					defender_drm += 1
				elif number_events == 2:
					defender_drm += 2
				elif number_events == 3:
					defender_drm += 3

			attacker_roll = (random.randint(1, 6)) + attacker_drm
			defender_roll = random.randint(1, 6) + defender_drm
			print(attacker_roll)
			print(defender_roll)
		else:
			move_reduce = input(f'How many movement points(Remaining: {move_points})?')
			move_points -= int(move_reduce)
	print('Run out of movement points...')
