import random

weather = input('Weather: Fair(f), Poor(p), or Severe(s)?')
loop = 0
while loop == 0:
	attacker_drm = 0
	defender_drm = 0
	move_points = 0
	unit = input('Unit: German(g), Soviet(s), or Axis Minor?')
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
		question = input('Attack(a), movement(m), finish activation(f)?')
		if question == 'a':
			move_reduce = input(f'How many movement points this attack(Remaining: {move_points})?')
			move_points -= int(move_reduce)
			print('ATTACKER FIRST!!!')
			if unit == 'g':
				attacker_drm += 2
				if unit_type == 'm' and weather == 'f':
					attacker_drm += 2
				elif unit_type == 'm' and weather == 'p':
					attacker_drm += 1
			if unit == 's' and unit_type == 'm':
				s_tanks = input("Tank unit?")
				if s_tanks == 'y':
					if weather == 'f':
						attacker_drm += 2
					elif weather == 'p':
						attacker_drm += 1
			air_support = input('Air support?')
			if air_support == 'y':
				if weather =='f':
					attacker_drm += 2
				elif weather == 'p':
					attacker_drm += 1
			river = input('Attacking across river?')
			if river == 'y':
				attacker_drm -= 1
			isolated_defender = input('Attacking isolated defender?')
			if isolated_defender == 'y':
				attacker_drm += 2
			city = input('Attacking city hex or rough terrain?')
			if city == 'y':
				attacker_drm -= 1
			if city != 'y':
				strait = input('Attacking across a strait hex side?')
				if strait == 'y':
					attacker_drm -= 2
			if unit == 's':
				elite = input('Elite unit(star symbol)?')
				if elite == 'y':
					attacker_drm += 1
			reduced = input('Reduced strength?')
			if reduced == 'y':
				attacker_drm -= 2
			low = input('Low supply?')
			if low == 'y':
				attacker_drm -= 2
			if unit == 's' and unit_type == 'l':
				shock = input('Shock unit in fair weather?')
				if shock == 'y':
					attacker_drm += 1
			if weather == 'p':
				attacker_drm -= 2
			assault = input('Assault (+2 for each tank or shock or +1 for any in severe) max 2 extra units?')
			if assault == 'y' and (weather == 'f' or weather == 'p'):
				number_assault = input('How many points?')
				if number_assault == 1:
					attacker_drm += 1
				elif number_assault == 2:
					attacker_drm += 2
				elif number_assault == 3:
					attacker_drm += 3
				else:
					attacker_drm += 4
			elif assault == 'y' and weather == 's':
				number_assault = input('How many points(max 2)?')
				if number_assault == 1:
					attacker_drm += 1
				else:
					attacker_drm += 2
			events = input('Tanks event(+2,+1)(except shock unit), Heavy Arty(+2) or Ground Support(+1)?')
			if events == 'y':
				number_events = input('How many points?')
				if number_events == 1:
					attacker_drm += 1
				elif number_events == 2:
					attacker_drm += 2
				elif number_events == 3:
					attacker_drm += 3
			print('NOW DEFENDER!!!')
			if unit != 'g':
				germ = input('German unit?')
				if germ == 'y':
					defender_drm += 2
			reduced = input('Reduced strength?')
			if reduced == 'y':
				defender_drm -= 2
			low = input('Low supply?')
			if low == 'y':
				defender_drm -= 2
			if unit != 's' and weather == 'f':
				shock = input('Shock unit?')
				if shock == 'y':
					defender_drm += 1
			tank_fair = input('Tank unit?')
			if tank_fair == 'y' and weather == 'f':
				defender_drm += 2
			elif tank_fair == 'y' and weather == 'p':
				defender_drm += 1
			air_support = input('Air support?')
			if air_support == 'y' and weather == 'f':
				defender_drm += 2
			elif air_support == 'y' and weather == 'p':
				defender_drm += 1
			if unit != 's':
				elite = input('Elite unit(star symbol)?')
				if elite == 'y':
					defender_drm += 1
			events = input('Tanks event(+2,+1)(except shock unit), Heavy Arty(+2) or Ground Support(+1)?')
			if events == 'y':
				number_events = input('How many points?')
				if number_events == 1:
					defender_drm += 1
				elif number_events == 2:
					defender_drm += 2
				elif number_events == 3:
					defender_drm += 3

			attacker_roll = random.randint(1, 6)
			defender_roll = random.randint(1, 6)
			attacker_total = attacker_roll + attacker_drm
			defender_total = defender_roll + defender_drm
			print(f'RESULT!!!')
			print(f'Attacker result: {attacker_total}, dice roll: {attacker_roll}, DRM: {attacker_drm}')
			print(f'Defender result: {defender_total}, dice roll: {defender_roll}, DRM: {defender_drm}')
			print(f'Unit out of supply roll divided by 2 round up')
			attacker_drm = 0
			defender_drm = 0
		elif question == 'm':
			move_reduce = input(f'How many movement points(Remaining: {move_points})?')
			move_points -= int(move_reduce)
		elif question == 'f':
			move_points -= move_points
		else:
			continue
	print('Run out of movement points...')
