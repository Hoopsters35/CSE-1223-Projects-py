import random

n1 = int(20 *random.random() + 1)
n2 = int(20 *random.random() + 1)
cor = 0

name = input('Enter your name: ')
print('Welcome ' + name + ' please answer the following questions:\n')
ans = int(input(str(n1) + ' + ' + str(n2) + ' = '))
if ans == n1 + n2:
	print('Correct!\n')
	cor += 1
else:
	print('Wrong!\nThe correct answer is ' + str(n1 + n2) + '\n')
	
	
ans = int(input(str(n1) + ' * ' + str(n2) + ' = '))
if ans == n1 * n2:
	print('Correct!\n')
	cor += 1
else:
	print('Wrong!\nThe correct answer is ' + str(n1 * n2) + '\n')
	
	
ans = int(input(str(n1) + ' / ' + str(n2) + ' = '))
if ans == n1 // n2:
	print('Correct!\n')
	cor += 1
else:
	print('Wrong!\nThe correct answer is ' + str(n1 // n2) + '\n')
	
	
ans = int(input(str(n1) + ' % ' + str(n2) + ' = '))
if ans == n1 % n2:
	print('Correct!\n')
	cor += 1
else:
	print('Wrong!\nThe correct answer is ' + str(n1 % n2) + '\n')
	
print('\nYou got ' + str(cor) + ' correct answers')
print("That's " + str(100 * cor / 4) + "%")