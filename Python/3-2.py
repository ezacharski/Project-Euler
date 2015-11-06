#Written by Edwin Zacharski
import math
cap = 600851475143
caproot = math.sqrt(cap)
caproot = math.floor(caproot)  #Square root of the number we are looking at, this is the highest possible factor
largestfactor = 0
primefinder = 2   #Starts the counter off at 2, don't need to check 1
factorfinder = 2
while factorfinder <= caproot:        #While loop checks number against the square root of number
	if cap % factorfinder == 0:
		print (factorfinder," is a factor of ",cap)
		primefinder = 2
		while primefinder <= factorfinder:   #Checks the factor that was found to see if it is prime
			if factorfinder % primefinder == 0:
				if primefinder == factorfinder:
					largestfactor = factorfinder
					break
				elif primefinder != factorfinder:
					print (factorfinder," is not a prime factor")
					break
			primefinder = primefinder + 1
	factorfinder = factorfinder + 1
print (largestfactor, " was the largest prime factor found")
