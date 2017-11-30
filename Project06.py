def makeList(input):
	num = []
	for i in input:
		num.append(int(i))
	return num
def getCD(num):
	num = num[::-1]
	sum = 0
	for i in range (1,len(num), 2):
		num[i] *= 2
		if num[i] >= 10:
			num[i] -= 9
	for i in range(1, len(num)):
		sum += num[i]
	if sum % 10 == 0:
		return 0
	else:
		return 10 - sum % 10
		
def getValidNum():
	yes = input('Enter a credit card number (enter a blank line to quit)')
	while yes and not len(yes) == 16:
		print('ERROR! Number MUST hae exactly 16 digits\n')
		yes = input('Enter a credit card number (enter a blank line to quit)')
	return yes


theirs = getValidNum()
while theirs:
	list = makeList(theirs)
	corD = getCD(list)
	print('Check digit should be:', str(corD))
	print('Check digit is', list[len(list) - 1])
	if corD == list[len(list) - 1]:
		print('Number is valid\n')
	else:
		print('Number is not valid\n')
	theirs = getValidNum()
print('Goodbye!')
	
