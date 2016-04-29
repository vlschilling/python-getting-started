
count=0
total=0

while True:
	usrinp = raw_input('Enter a number: ')
	if usrinp == 'done':
		break
	try:
		number = float(usrinp)
	except:
		print "Nope, try again"
		continue
	count = count+1
	total = total+number
	#print number,total,count

print 'Total: ',total,"\n",'Count: ',count,'\n','Average: ',total/count,'\n'


