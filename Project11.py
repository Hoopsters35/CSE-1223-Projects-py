def readNextSeries(inFile):
	list = []
	temp = int(inFile.readline())
	list.append(temp)
	while not temp == -1:
		temp = int(inFile.readline())
		list.append(temp)
	list.remove(-1)
	return list
	
def getMedian(numList):
	median = 0
	numList.sort()
	if len(numList) % 2 == 0:
		median = (numList[len(numList)//2] + numList[len(numList)//2 - 1]) / 2
	elif len(numList) % 2 == 1:
		median = numList[len(numList)//2]
	return median

def getMean(numList):
	sum = 0
	for i in range(len(numList)):
		sum += numList[i]
	return sum // len(numList)
	
def getMax(numList):
	max = numList[0]
	for i in range(len(numList)):
		if numList[i] > max:
			max = numList[i]
	return max

def getMin(numList):
	min = numList[0]
	for i in range(len(numList)):
		if numList[i] < min:
			min = numList[i]
	return min
	
def getInFile():
	str = input("Please enter the input file name: ")
	try:
		file = open(str, "r")
		return file
	except:
		print('Error with input file')
	
	
def getOutFile():
	str = input('Please enter the output file name: ')
	try:
		file = open(str, "w")
		return file
	except:
		print('Error with output file')
	
	
def getSoreSummary(scores):
	totalSummary = []
	for i in range(len(scores)):
		summary = []
		summary.append(getMean(scores[i]))
		summary.append(getMedian(scores[i]))
		summary.append(getMax(scores[i]))
		summary.append(getMin(scores[i]))
		totalSummary.append(summary)
	return totalSummary
	
def getMaxNameLength(names):
	maxL = 0
	for i in names:
		if len(i) > maxL:
			maxL = len(i)
	return maxL

def getMaxAvg(scoreSummary):
	maxA = 0
	maxIndex = 0
	
	for i in range(len(scoreSummary)):
		if scoreSummary[i][0] > maxA:
			maxA = scoreSummary[i][0]
			maxIndex = i
	out = [maxIndex, maxA]
	
	return out
	
def getMinAvg(scoreSummary):
	minA = 150
	minIndex = 0
	
	for i in range(len(scoreSummary)):
		if scoreSummary[i][0] < minA:
			minA = scoreSummary[i][0]
			minIndex = i
	out = [minIndex, minA]
	
	return out
	
def writeOutput(outFile, names, scoreSummary):
	maxL = getMaxNameLength(names) + 2
	dashes = '-'*maxL
	string = "%-" + str(maxL) + "s   %6s %6s %4s %4s"
	outFile.write(string % ("Name", "Mean", "Median", "Max", "Min"))
	outFile.write('\n')
	string = "%-1." + str(maxL) + "s   %.6s %.6s %.4s %.4s"
	outFile.write(string % (dashes, dashes, dashes, dashes, dashes))
	outFile.write('\n')
	for i in range(len(names)):
		string = "%-" + str(maxL) + "s   %6d %6d %4d %4d"
		outFile.write(string % (names[i], scoreSummary[i][0], scoreSummary[i][1], scoreSummary[i][2], scoreSummary[i][3]))
		outFile.write('\n')
	outFile.write('Total number of participants: ' + str(len(names)) + '\n')
	maxA = getMaxAvg(scoreSummary) 
	outFile.write('Highest average score: ' + names[maxA[0]] + ' (' + str(maxA[1]) + ')\n')
	minA = getMinAvg(scoreSummary)
	outFile.write('Lowest average score: ' + names[minA[0]] + ' (' + str(minA[1]) + ')')
	
names = []
scores = []
inFile = getInFile()
outFile = getOutFile()

for line in inFile: 
	oneName = line
	names.append(oneName)
	tempList = readNextSeries(inFile)
	scores.append(tempList)

for i in range(len(names)):
	names[i] = names[i].replace("\n", "")

scoreSummary = getSoreSummary(scores)
writeOutput(outFile, names, scoreSummary)	

inFile.close()
outFile.close()