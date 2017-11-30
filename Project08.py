def promptForDecimal():
	inp = input('Enter an Integer value (negative value to quit): ')
	while not (inp.isdigit() or inp[:1] == '-' and inp[1].isdigit()):
		print("ERROR - value must be a number")
		inp = input('Enter an Integer value (negative value to quit): ')
	return int(inp)
	
def decimalToBinary(value):
	out = ""
	if value == 0:
		out = '0'
	while not value == 0:
		out = str(value % 2) + out
		value //= 2
	return out

print('Converting from Decimal to Binary')
num = promptForDecimal()
while num >= 0:
	bin = decimalToBinary(num)
	print('The decimal value', num, 'is', bin, 'in binary.\n')
	num = promptForDecimal()
print('Goodbye')