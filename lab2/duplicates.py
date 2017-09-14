#!/usr/bin/python3
#Created by Harrison Barnett 11 Aug 17
#Created for Comp1531 Lab2 Exercise

s = input("Please enter a string: ") #input is saved in variable "s"

words_list1 = s.split() #List of words from the string "s" that have been seperated (split) via space and are all lower case

words = {} #Create an array (dictionary) called "words" that is currently empty
newString = []



for word in words_list1:
    if word.lower() not in words:
        words[word.lower()]=1
        newString.append(word)
		
newString = sorted(newString, key=lambda x: x.lower())

new_string = ' '.join(words)
print(new_string)



