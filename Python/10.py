#Written by Edwin Zacharski
#Project Euler problem #10

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
				primetally = currentnum + primetally
				print("The current number is: ", currentnum, "The current sum is ", primetally)
				break
			elif currentnum != count:
#					print (currentnum," is not a prime number")
					break
		count = count + 1
	currentnum = currentnum + 1
	count = 2
if primetally == 2000000:
		foundallprimes = True
print ("The sum of all prime numbers under 2,000,000 is: ", highestprime)
