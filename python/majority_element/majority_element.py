# uses python3
#
# Written by: Stephen Jonker
# Written on: Wednesday 27 Sept 2017
# Copyright (c) 2017 Stephen Jonker - www.stephenjonker.com
#
# Overview:
# - majority_element 
# - Data Structures and Algorithms 
# 
# Purpose:
# - write a majority_element algorithm using recursive divide and conquer
# - The Majority Element
# - Given a list of integer values, the a majority element exist if it occurs 
#   greater than 50% of the time. 
# - Eg. 
# - Given the 5 element list: 1 2 2 2 7 
# - A majority element exists, and it is "2" 
#
# Input:
# - a series of integer numbers, where n >= 0
# - 2 lines of input are taken from STDIN 
# - First line: a single integer indicating the number of elements in the second line
# - Second line: the N number of elements that will be searched to determine if a majority 
#   elemnt exists
#
# Output: 
# - 1 for majority element exists
# - 0 for majority element DOES NOT exist
# 
# Constraints: 
# 
# element in the list: 1 <= element <= 10**9
# input is sorted for (a) 
#
# Usage:
# 	python3 majority_element
# 	5 
# 	1 2 2 2 7 
# 	1 
#
# Testing:
# - unit test for this code can be found in: test_majority_element.py
# 
# Test usage:
# 	pthon3 test_majoriity_element -v 
# 

def countElementInList(listOfElements, item):
	# use linear method
	cnt = 0 
	for i in listOfElements:
		if item == i:
			cnt = cnt + 1

	return cnt

def majority_element_divide_and_conquer(listOfElements):
	#
	# Use "linear search" to find if majority element exists
	#
	# Input: 
	# - listOfElements is a list of integer values that will be searched for a majority element
	# E.g 
	# [1, 2, 3, 2, 2]
	#
	# Output: 
	# - 1 for majority element exists
	# - 0 for majority element DOES NOT exist
	#

	#
	# Created an inner version of recursive routine
	# for recursion to work, routine must return the actual
	# majority elemtent, but the purpose it to just check if 
	# it is there or not and return 1=yes, 0=no.  So 
	# put a wrapper around it to sort things out.
	#
	def me_div_and_con(listOfElements):
		result = 0 

		debug = False

		# code goes here
		n = len(listOfElements) 
		if n == 1:
			return listOfElements[0]
		k = n//2 # Python3 integer division
		
		rightSide = listOfElements[k:]
		leftSide = listOfElements[0:k]

		if debug:
			print()
			print(">>> n: ", n)
			print(">>> k: ", k)
			print(">>> listOfElements: ", listOfElements)	
			print(">>> rightSide: ", rightSide)
			print(">>> leftSide: ", leftSide)
			# quit() 

		itemRightSide = me_div_and_con(rightSide)
		itemLeftSide = me_div_and_con(leftSide)

		if itemLeftSide == itemRightSide:
			return itemLeftSide

		itemLeftSideCount = countElementInList(listOfElements, itemLeftSide)
		itemRightSideCount = countElementInList(listOfElements, itemRightSide)
		if itemLeftSideCount > k:
			return itemLeftSide
		if itemRightSideCount > k:
			return itemRightSide

		return -1  
	#
	# This is just a wrapper around the recursive routine to sort out
	# the returned result. Ie translate between a majority element found 
	# and majority element exists or not. 
	# 
	# Plus, do not have to make changes to test units :-) 
	# 
	result = 0 
	r = me_div_and_con(listOfElements)
	if r >= 0:
		result = 1

	return result

def majority_element_linear_search(listOfElements):
	#
	# Use "linear search" to find if majority element exists
	#
	# Input: 
	# - listOfElements is a list of integer values that will be searched for a majority element
	# E.g 
	# [1, 2, 3, 2, 2]
	#
	# Output: 
	# - 1 for majority element exists
	# - 0 for majority element DOES NOT exist
	#
	result = 0 

	# code goes here
	n = len(listOfElements)
	k = n//2 	# python3 integer division
	for i in listOfElements:
		count = 0 
		for g in listOfElements:
			if g == i:
				count = count + 1
		if count > k:
			result = 1
			break 

	return result

def doStuff(listOfElements):
	#
	# this is the "main" program driver rountine
	# 
	# Input:
	# - listOfElements: list of non-sorted integer values 
	#
	# Output:
	# - 1 if majority element exists
	# - 0 if majority elemtnt DOES NOT exist 
	#

	result = 0

	# Code goes here
	result = majority_element_divide_and_conquer(listOfElements)
	
	return result

def displayOutput(res):
	#
	# Input:
	# - res -> is a single integer  
	# - Eg. 1
	#
	# Output:
	# - 0 | 1 
	# E.g.
	# 1
	# 
	# Note: yes, I do not need a function to output a single integer...
	# 		developing a programm pattern for this type of problem that 
	# 		using....
	# 		getInput() 
	# 		doStuff()
	# 		displayOutput() 
	# 
	print(str(res))

def getInput_n():

	result = int(input())
	return result


def getInput_list():
	# Input:
	# - None
	# Output:
	# - list of integer values 
	# E.g 
	# [5 1 5 8 12 13]
	# 

	debug = False

	# Get rest of input
	#
	inputData = []

	inputData = list(map(int, input().split() ))

	if debug: print(">>> inputData: " + str(inputData))

	return inputData

def runProgram():

	# Get number of elements, not really needed
	# get it and thow it away so program works
	# 
	n = getInput_n()

	# Get rest of input
	#
	inputData = getInput_list() 
	
	res = doStuff(inputData)
	displayOutput(res)

if __name__ == "__main__":

	runProgram() 
	
#
# End of file.
#
