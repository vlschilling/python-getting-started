def computepay(a,b):
	if hours <= 40:
		gross = a*b
	else:
		ot = a - 40
		gross = (ot*b*1.5)+(40*b)
	return gross

try:
	userinp = raw_input('Enter hours: ')
	hours = float(userinp)
	userinp = raw_input('Enter rate: ')
	rate = float(userinp)
except:
	print 'Wrong, enter a number next time!'
	quit()

###previous version of script###
#if hours <= 40:
#	pay = hours*rate
#else:
#	ot = hours - 40
#	pay = (ot*rate*1.5)+(40*rate)
#####

pay = computepay(hours,rate)

print 'Pay: ', pay


