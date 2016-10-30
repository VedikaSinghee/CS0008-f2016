def main():
	# initalize the total variables to 0
	totalNumLines = 0
	totalDistance = 0
	while(True):
		# reading the filename
		filename = input('File to be read: ')

		#if the filename is empty, q or quit, we exit the loop
		if filename == '' or filename == 'q' or filename == 'quit':
			break

		# otherwise we process the file
		# create the file handler to read from the file
		fh = open(filename, 'r')
		(partialNumLines, partialDistance) = processFile(fh)

		# print the partial num lines and partial distance
		printKV('Partial Total # of lines', partialNumLines, 30)
		printKV('Partial distance run', partialDistance, 30)

		# add the partial data to the total data
		totalNumLines += partialNumLines
		totalDistance += partialDistance

	# finally print out the totals
	print('Totals')
	printKV('Total # of lines', totalNumLines, 30)
	printKV('Total distance run', totalDistance, 30)

def processFile(fh):
	# initializing the variables to 0
	numLines = 0
	totalDistance = 0
	# iterating through every line in the file
	for line in fh:
		# removing the '\n' from the end of the line
		line = line.rstrip()
		# separating the name and distance in the line
		(name, distance) = line.split(",", 2)
		# adding the distance to the total distance
		totalDistance += float(distance)
		# incrementing the number of lines read
		numLines += 1

	return (numLines, totalDistance)

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
