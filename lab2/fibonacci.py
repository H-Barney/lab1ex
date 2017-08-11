#!/usr/bin/python3
#Created by Harrison Barnett 11 Aug 17
#Created for Comp1531 Lab2 Exercise
s=int(input("How many numbers in series?: "))

count = 0
fib1 = 1
fib2 = 0
temp = 0
while (count < s):
	if count <= 0:
		print("1")
		count = count+1
	else:
		print(fib1+fib2)
		temp = fib2
		fib2 = fib1
		fib1 = fib1+temp
		count = count+1

