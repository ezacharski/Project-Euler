import math
cap = 600851475143
factorfinder = 2
primefinder = 2
caproot = math.sqrt(cap)
caproot = math.floor(caproot)
largestfactor = 0
for factorfinder in range(2,caproot):
	if cap % factorfinder == 0:
		print (factorfinder," is a factor of ",cap)
		for primefinder in range(2,factorfinder):
			print ("hello")
			if factorfinder % primefinder == 0:
				print (factorfinder," is not a prime factor")
				break
			else:
				largestfactor = factorfinder
				print ("Current largest prime factor is ", largestfactor)
				break
print (largestfactor, " was the largest prime factor found")
