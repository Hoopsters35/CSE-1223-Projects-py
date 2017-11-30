import random
def getBet(pool):
	print('You have', str(pool), 'dollars.')
	bet = int(input('Enter an amount to bet (0 to quit): '))
	while bet < 0 or bet > pool:
		print('ERROR: bet is outside acceptable range')
		bet = int(input('Enter an amount to bet (0 to quit): '))
	return bet
	
def getHighLow():
	hl = input('High, low or sevens (H/L/S): ')
	hl.lower()
	while not hl == 'h' or hl == 'l' or hl == 's':
		print('ERROR: Please use given format')
		hl = input('High, low or sevens (H/L/S): ')
	return hl

def getRoll():
	roll = int(random.random() * 6 + 1)
	return roll
	
def determineWinnings(hl, bet, roll):
	winnings = 0
	if hl == 'h' and roll >= 8 or hl == 'l' and roll <= 6:
		winnings = bet
		print('You won', str(winnings), 'dollars!')
	elif hl == 's' and roll == 7:
		winnings = 4 * bet
		print('You won', str(winnings), 'dollars!')
	else:
		winnings = 0-bet
		print('You lost!')
	print()
	return winnings
	
_pool = 100
while _pool > 0:
	_bet = getBet(_pool)
	if _bet == 0:
		print()
		break
	_hl = getHighLow()
	d1 = getRoll()
	d2 = getRoll()
	print('Die 1 rolls:', str(d1))
	print('Die 2 rolls:', str(d2))
	tot = d1+d2
	print('Total of two dice is', str(tot))
	_winnings = determineWinnings(_hl, _bet, tot)
	_pool += _winnings
print('You have', str(_pool), 'dollars left\nGoodbye!')