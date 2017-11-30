import random

def whoWins(theirD, myD):
	if theirD == 'Plant dragon' and myD == 'Fire dragon':
		print("Fire defeats Plant - you lose!")
		return 0
	elif theirD == 'Plant dragon' and myD == 'Water dragon':
		print("Plant defeats water - you win!")
		return 1
	elif theirD == 'Water dragon' and myD == 'Fire dragon':
		print('Water defeats Fire - you win!')
		return 1
	elif theirD == 'Water dragon' and myD == 'Plant dragon':
		print('Plant defeats Water - you lose!')
		return 0
	elif theirD == 'Fire dragon' and myD == 'Water dragon':
		print('Water defeats Fire - you lose!')
		return 0
	elif theirD == 'Fire dragon' and myD == 'Plant dragon':
		print('Fire defeats Plant - you win!')
		return 1
	else:
		print('A Tie!')
		return 2

numW = 0
numL = 0
numT = 0
while numW <2 and numL < 2:
	their_drag = input('Please select one of your dragoons [Fire/Plant/Water]: ')
	if their_drag.lower() == 'fire' or their_drag.lower() == 'f':
		their_drag = 'Fire dragon'
	elif their_drag.lower() == 'plant' or their_drag.lower() == 'p':
		their_drag = 'Plant dragon'
	elif their_drag.lower() == 'water' or their_drag.lower() == 'w':
		their_drag = 'Water dragon'
	print('You chose: ' + their_drag)
	ran = int(random.random() * 3)
	my_drag = 'none'
	if ran == 0:
		my_drag = 'Fire dragon'
	elif ran == 1:
		my_drag = 'Plant dragon'
	elif ran == 2:
		my_drag = 'Water dragon'
		
	print('I chose: ' + my_drag)
	res = whoWins(their_drag, my_drag)
	if res == 0:
		numL +=1
	elif res ==1:
		numW += 1
	elif res ==2:
		numT +=1
	print('\n')
print('Out of the ' + str(numT + numW + numL) + ' matches you won ' + str(numW) + ', I won ' + str(numL) + ', and we tied ' + str(numT) + '.')
if numW > numL:
	print('Congratulations - you win the tournament!')
else:
	print('I win! Better luck next time.')