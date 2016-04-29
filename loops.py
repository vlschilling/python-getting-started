
###infinite loop with break###
#while True:
#	line = raw_input('> ')
#	if line == 'done':
#		break
#	print line
#print 'Done!'



###infinite loop with continue###
#while True:
#	line = raw_input('> ')
#	if line[0] == '#':
#		continue
#	if line == 'done':
#		break
#	print line
#print 'Done!'



###definite loop with for###
#friends = ['Joe', 'Glenn', 'Sally']
#for friend in friends:
#	print 'Happy New Year:', friend
#print 'Done!'

###counting loop###
#count = 0
#for itervar in [3,41,12,9,74,15]:
#	count = count+1
#print 'Count: ', count


###summing loop###
#total = 0
#for itervar in [3,41,12,9,74,15]:
#	total = total + itervar
#print 'Total: ', total



###Maximum loop###
#largest = None
#print 'Before:', largest
#for itervar in [3,41,12,9,74,15]:
#	if largest is None or itervar > largest:
#		largest = itervar
#	print 'Loop:', itervar, largest
#print 'Largest:', largest


###Minimum loop###
smallest = None
print 'Before:', smallest
for itervar in [3,41,12,9,74,15]:
	if smallest is None or itervar < smallest:
		smallest = itervar
	print 'Loop:', itervar, smallest
print 'Smallest:', smallest


























