#Created by Harrison Barnett 11 Aug 17
#Created for Comp1531 Lab2 Exercise

s = input("Please enter a string") #input is saved in variable "s"

words_list = s.split() #List of words from the string "s" that have been seperated (split) via space

words = {} #Create an array (dictionary) called "words" that is currently empty

for word in words_list:  #Nested loop that adds +1 for every time it comes accross the same string
	if word not in words: #Each word is called individually by "word"
		words[word] = 1
	else:
		words[word] += 1


