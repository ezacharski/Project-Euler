sumofsquares = 0
squareofsums = 0
difference = 0
count = 1

while count <= 100:
	sumofsquares = (count * count) + sumofsquares
	squareofsums = count + squareofsums
	count = count + 1
squareofsums = squareofsums * squareofsums
difference = squareofsums - sumofsquares
print ("The difference is ", difference)
	
