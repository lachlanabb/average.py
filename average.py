# this is code that Mr. Jugoon wrote.
# the code responds to an individual's shape.

average = 0.0

total = 0 

for x in range(0, 1):
	
	grade1 = int(input("What was your 1st numerical grade?"))
	print("Your number is: " + str(grade1))
	grade2 = int(input("What is your 2nd number?"))
	print("Your number is: " + str(grade2))
	grade3 = int(input("What is your 3rd number?"))
	print("Your number is: " + str(grade3))
	grade4 = int(input("What is your 4th number?"))
	print("Your number is: " + str(grade4))
	grade5 = int(input("What is your 5th number?"))
	print("Your number is: " + str(grade5))
	total = total + grade1 + grade2 + grade3 + grade4 + grade5

average = total/5

print("The average of your five grades is: " + str(average))

	 



