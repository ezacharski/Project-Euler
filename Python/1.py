cap = 1000
total = 0
i = 1
while i < cap:
	if i % 5 == 0:
		total = total + i
		i = i + 1
	elif i % 3 == 0:
		total = total + i
		i = i + 1
	else:
		i = i + 1
print (total)