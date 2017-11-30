def promptForBinary():
	inp = input('Enter a binary value (empty line to quit): ')
	while not checkForBinaryValue(inp):
		inp = input('Please enter a valid binary value (empty line to quit): ')
	return inp
		
	
def checkForBinaryValue(value):
	bool = True
	if len(value) > 0:
		for i in value:
			if not i in "10":
				bool = False
	return bool

def binaryToDecimal(value):
	n = len(value) - 1
	deci = 0
	for i in value:
		deci += int(i) * 2**n
		n -=1
	return deci
			

bin = promptForBinary()
while len(bin) > 0:
	print('The binary value', bin, 'is', binaryToDecimal(bin), 'in decimal (base 10)\n')
	bin = promptForBinary()
	
print('Goodbye')
	