
largest=None
smallest=None

while True:
	usrinp = raw_input('Enter a number: ')
	if usrinp == 'done':
		break
	try:
		number = float(usrinp)
	except:
		print "Nope, try again"
		continue
	if largest is None or number > largest:
		largest = number
	if smallest is None or number < smallest:
		smallest = number

print "Max: ",largest,"Min :",smallest
