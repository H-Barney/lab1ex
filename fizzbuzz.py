number = input("Enter parameter ")
print "Input was", int(number)
count = 1
while(count < int(number)):
	if(count%3 == 0 and count%5 == 0):
		print "fizzbuzz"
	elif(count%3 == 0):
		print "fizz"
	elif(count%5 == 0):
		print"buzz"
	else:
		print count
	count = count + 1
	
