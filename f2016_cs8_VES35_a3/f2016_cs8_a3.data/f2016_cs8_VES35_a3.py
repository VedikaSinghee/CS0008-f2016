def main():
	# initalize the total variables to 0
	totalNumLines = 0
	totalDistance = 0
	totalFiles = 0
	# dictionary mapping each participant to their total distance
	participantDirectory = {}
	# dictionary mapping each participant to their frequency
	frequencyD = {}
	# counter to track participants with multiple occ
	mult = 0
	# Reading the input filename of the master input file
	filename = input('Master input file to be read: ')
	#if the filename is empty, q or quit, we exit the loop
	if filename == '' or filename == 'q' or filename == 'quit':
		print("Invalid filename. Run again...")

	with open(filename) as fh:
		files = fh.readlines()
		fh.close()

	for file in files:
		totalFiles += 1
		# otherwise we process the file
		# create the file handler to read from the file
		fh = open(file.rstrip(), 'r')
		(partialNumLines, partialDistance, participantDirectory, mult, frequencyD) = processFile(fh, participantDirectory, mult, frequencyD)
		# add the partial data to the total data
		totalNumLines += partialNumLines
		totalDistance += partialDistance
		# closing the file
		fh.close()
	
	# Find the maxmimums and minimums
	(maxD, maxN, minD, minN) = findMaxMin(participantDirectory)

	# print out the totals
	printKV('Number of input files read', totalFiles, 30)
	printKV('Total number of lines read', totalNumLines, 30)
	printKV('Total distance run', totalDistance, 30)
	print("Max distance run : ",maxD)
	print("  by participant : ", maxN)
	print("Min distance run : ",minD)
	print("  by participant : ", minN)
	print("Total Number of Participants ", len(participantDirectory))
	print("Number of Participants with multiple occurrences ", mult)

	# writing output
	with open("f2016_cs8_vs35_a3.data.output.csv",'w') as compiled:
		names = list(participantDirectory.keys())
		for name in names:
			# explicitly putting commas as output file is CSV
			compiled.write(name + "," + str(frequencyD[name]) + "," + str(participantDirectory[name]) + "\n")

def processFile(fh, participantDirectory, mult, frequencyD):
	# initializing the variables to 0
	numLines = 0
	totalDistance = 0
	isFirstLine = True
	# iterating through every line in the file
	for line in fh:
    	# Ignoring the first line since it contains headers for columns
		if (isFirstLine):
			isFirstLine = not(isFirstLine)
			continue
		else:
			# removing the '\n' from the end of the line
			line = line.rstrip()
			# separating the name and distance in the line
			(name, distance) = line.split(",", 2)
			# adding name to participant dictionary {name: distance}
			# adding name to frequency dictionary {name: frequency}
			# If name is already there then this participant has multiple (>1) occurrences
			if name in participantDirectory:
				mult += 1
				participantDirectory[name] += float(distance)
				frequencyD[name] += 1
			else:
				participantDirectory[name] = float(distance)
				frequencyD[name] = 1

			# adding the distance to the total distance
			totalDistance += float(distance)
			# incrementing the number of lines read
			numLines += 1

	return (numLines, totalDistance, participantDirectory, mult, frequencyD)

def findMaxMin(D):
	distances = list(D.values())
	names = list(D.keys())
	# maximum
	maxD = max(distances)
	maxN = names[distances.index(maxD)]
	# minimum
	minD = min(distances)
	minN = names[distances.index(minD)]
	return (maxD, maxN, minD, minN)

def printKV(key, value, klen = 0):
	# the key is formatted as the max between the length of the key and klen
	nLength = max(klen, len(key))
	# setting the key to be printed with the number of spaces calculated above
	keyOutput = '{:{n}s} : '.format(key, n=nLength)
	# setting the value to be printed in the given format
	if isinstance(value, str):
		# if it is a string it should be 20 spaces long
		valOutput = '{:{n}s} : '.format(value, n=20)
	elif isinstance(value, int):
		# if it is an integer it should be 10 spaces long
		valOutput = '{0:10d}'.format(value)
	elif isinstance(value, float):
		# if it is a float it should be 10 spaces long with 3 decimals
		valOutput = '{0:10.3f}'.format(value)
	else:
		# in all other cases no formatting is required
		valOutput = value

	# printing the key and value
	print(keyOutput, valOutput)

if __name__ == "__main__":
    main()
