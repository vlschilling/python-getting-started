try:
	userinp = raw_input('Enter hours: ')
	hours = float(userinp)
	userinp = raw_input('Enter rate: ')
	rate = float(userinp)
except:
	print 'Wrong, enter a number next time!'
	quit()
if hours <= 40:
	pay = hours*rate
else:
	ot = hours - 40
	pay = (ot*rate*1.5)+(40*rate)
#pay = float(hours) * float(rate)
print 'Pay: ', pay


