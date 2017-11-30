full = str(input('Enter the full string: '))
sub = str(input('Enter the substring: '))
print('Length of your string is: ' + str(len(full)))
print('Length of your substring is: ' + str(len(sub)))
begIdx = full.index(sub)
bef = full[:begIdx]
print('Starting position of your substring in string: ' + str(begIdx))
print('String before your substring: ' + bef)
aft = full[begIdx + len(sub)::1]
print('String after your substring: ' + aft)
pos = int(input('Enter a position between 0 and ' + str(len(full)) + " "))
print("The character at position " + str(pos) + " is " + str(full[pos:pos + 1]))
rep = input('Enter a replacement string: ')
print('Your new string is: ' + bef + rep + aft)