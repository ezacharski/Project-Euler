foundnumber = False
smallestmultiple = 0
count = 20
while foundnumber == False:
	if count % 20 == 0:
		if count % 19 == 0:
			if count % 18 == 0:
				if count % 17 == 0:
					if count % 16 == 0:
						if count % 15 == 0:
							if count % 14 == 0:
								if count % 13 == 0:
									if count % 12 == 0:
										if count % 11 == 0:
											if count % 10 == 0:
												if count % 9 == 0:
													if count % 8 == 0:
														if count % 7 == 0:
															if count % 6 == 0:
																if count % 5 == 0:
																	if count % 4 == 0:
																		if count % 3 == 0:
																			if count % 2 == 0:
																				smallestmultiple = count
																				foundnumber = True
	count = count + 1
print ("The smallest multiple is ", smallestmultiple)
