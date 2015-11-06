cap = 4000000
first = 1
second = 2
temp = 0
total = 0
while first < cap:
	if first % 2 == 0:
		total = total + first
		temp = first + second
		first = second
		second = temp
	else:
		temp = first + second
		first = second
		second = temp
print (total)