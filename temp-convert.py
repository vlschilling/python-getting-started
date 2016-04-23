userinp = raw_input('What is the temperature in Celsius? ')
try:
	celsius = float(userinp)
	conv_temp = celsius * 1.8 + 32
	print celsius, ' degrees Celsius\n',conv_temp, ' degrees Farenheit'
except:
	print "Please enter a number"
