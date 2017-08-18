#!/usr/bin/python3
#Created by Harrison Barnett 11 Aug 17
#Created for Comp1531 Lab2 Exercise

s = input("Please enter a string: ") #input is saved in variable "s"

words_list = s.split() #List of words from the string "s" that have been seperated (split) via space

words = {} #Create an array (dictionary) called "words" that is currently empty
print_words = {}

for word in words_list:  #Nested loop that adds +1 for every time it comes accross the same string
	if upper(word) not in upper(words): #Each word is called individually by "word"
		words[word] = word

for word in words:
	print(words[word])


