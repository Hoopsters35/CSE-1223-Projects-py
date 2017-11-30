from random import randint

def resetDice(dice):
	for i in dice:
		i = 0
		
def rollDice(dice):
	for i in range(len(dice)):
		if dice[i] == 0:
			dice[i] = randint(1,10)

def diceToString(dice):
	return str(dice).replace('[', '').replace(']', '').replace(',', '')
	
def checkValidIndex(num):
	while num < -1 or num > 4:
		num = int(input("ERROR: Must select index between 0 and 4 (-1 to keep remaining dice): "))
	return num
	
def promptForReroll(dice):
	print(diceToString(dice))
	index = int(input('Select a die to re-roll (-1 to keep remaining dice): '))
	index = checkValidIndex(index)
	
	while index >= 0:
		dice[index] = 0
		print(diceToString(dice))
		index = int(input('Select a die to re-roll (-1 to keep remaining dice): '))
		index = checkValidIndex(index)
		
	print('Keeping remaining dice...\nRerolling...')
	
def promptForPlayAgain():
	bool = False
	tmp = input('Would you like to play again [Y/N]?: ')
	if tmp.lower() == 'y':
		bool = True
	print()
	return bool
	
def getCounts(dice):
	list = [0 for i in range(10)]
	for o in range(10):
		for i in dice:
			if i == o + 1:
				list[o] += 1
	print(list)
	return list
	
def checkStraight(counts):
	index = 0
	numOnes = 0
	if 1 in counts:
		while not counts[index] == 1:
			index += 1
		while counts[index] == 1:
			numOnes += 1
			index += 1
		if numOnes == 5:
			return True
	return False
		
def getResult(counts):
	res = [None for i in range(8)]
	if 5 in counts:
		res[0] = "Five of a Kind!"
	elif 4 in counts:
		res[1] = "Four of a Kind!"
	elif 3 in counts:
		res[3] = "Three of a Kind!"
		if 2 in counts:
			res[2] = "Full House!"
	elif 2 in counts:
		res[6] = "One Pair!"
	twoC = 0
	maxN = 0
	maxNCounter = 0
	for i in counts:
		maxNCounter += 1
		if i == 2:
			twoC += 1
		if i > 0:
			maxN = maxNCounter
		
	if twoC > 1:
		res [5] = 'Two Pair'
	res[7] = "High card: " + str(maxN)
	if checkStraight(counts):
		res[4] = 'Straight!'
	#decide which to return
	for i in res:
		if i:
			return i
	
#main
play = True
while play:
	dice = [0 for i in range(5)]
	rollDice(dice)
	promptForReroll(dice)
	rollDice(dice)
	print('Your final dice:', diceToString(dice))
	counts = getCounts(dice)
	print(getResult(counts))
	play = promptForPlayAgain()
print('Goodbye!')


			
		
	