def computeGrade(x):
	#check that the number is in correct range
	if x < 0.0 or x > 1.0:
		print "Input a number between 0 and 1"
		quit()
	#calculate the grade
	if x >= 0.9:
		y="A"
	elif x < 0.9 and score >=0.8:
		y="B"
	elif x < 0.8 and score >=0.7:
		y="C"
	elif x < 0.7 and score >= 0.6:
		y="D"
	else:
		y="F"
	return y

#get user input & verify that it is a number
try:
	userinp = raw_input("What is your score? ")
	score=float(userinp)
except:
	print "Input a number!"
	quit()

###previous script###
#if score < 0.0 or score > 1.0:
#	print "Input a number between 0 and 1"
#	quit()
#if score >= 0.9:
#	grade="A"
#elif score < 0.9 and score >=0.8:
#	grade="B"
#elif score < 0.8 and score >=0.7:
#	grade="C"
#elif score < 0.7 and score >= 0.6:
#	grade="D"
#else:
#	grade="F"

#call the function
grade = computeGrade(score)

#output the result
print "Your grade is: ",grade



