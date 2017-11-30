import random

numGuess = 0
num = int(random.random() * 200 + 1)

guess = int(input('Enter a guess between 1 and 200: '))
while not guess == num:
	numGuess +=1 
	if guess > num:
		print('Your guess was too high. Try again.\n')
	else:
		print('Your guess was too low. Try again.\n')
	guess = int(input('Enter a guess between 1 and 200: '))
print('Congratulations! Your guess was correct!\n')
print('I had chosen', str(num), 'as the target number.')
print('You guessed it in', str(numGuess), 'tries.')
if numGuess == 1:
	print('That was astounding!')
elif numGuess <= 4:
	print('That was lucky!')
elif numGuess <= 6:
	print('That was pretty good.')
elif numGuess <= 7:
	print('That was not that impressive.')
elif numGuess <= 9:
	print('Are you sure this is the right game for you?')
else: print("This just isn't your game is it?")