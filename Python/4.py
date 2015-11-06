firstnum = 1
secondnum = 1
product = 0
largestpal = 0
while firstnum < 1000:
	while secondnum < 1000:
		product = firstnum * secondnum
		if str(product) == str(product)[::-1]:
			if product > largestpal:
				largestpal = product
			print(firstnum, " times ", secondnum, " is ", product, ", which is a palindrome")
		secondnum = secondnum + 1
	firstnum = firstnum + 1
	secondnum = 1
print ("The largest palindrome number found was ", largestpal)
