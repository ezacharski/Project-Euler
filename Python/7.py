#Written by Edwin Zacharski
#For Project Euler Problem #7, finds the 10,001st prime number
#The comments help to see where it is in the calculation
foundprime = False
foundallprimes = False
primetally = 0
count = 2
currentnum = 2
highestprime = 0
while foundallprimes == False:
	while count <= currentnum:
#		print ("currently seeing if ",currentnum, "is divisible by ", count)
		if currentnum % count == 0:
			if currentnum == count:
				primetally = primetally + 1
#				print("Prime #", primetally, " is", currentnum)
				highestprime = currentnum
				break
			elif currentnum != count:
#					print (currentnum," is not a prime number")
					break
		count = count + 1
	currentnum = currentnum + 1
	count = 2
	if primetally == 10001:
		foundallprimes = True
print ("The 10,001st Prime is: ", highestprime)
