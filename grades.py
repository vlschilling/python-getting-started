try:
	userinp = raw_input("What is your score? ")
	score=float(userinp)
except:
	print "Input a number!"
	quit()
if score < 0.0 or score > 1.0:
	print "Input a number between 0 and 1"
	quit()
if score >= 0.9:
	grade="A"
elif score < 0.9 and score >=0.8:
	grade="B"
elif score < 0.8 and score >=0.7:
	grade="C"
elif score < 0.7 and score >= 0.6:
	grade="D"
else:
	grade="F"
print "Your grade is: ",grade