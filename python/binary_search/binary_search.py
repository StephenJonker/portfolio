# uses python3
#
# Written by: Stephen Jonker
# Written on: Tuesday 26 Sept 2017
# Copyright (c) 2017 Stephen Jonker - www.stephenjonker.com
#
# Overview:
# - binary_search 
# - Data Structures and Algorithms 
# 
# Purpose:
# - write a binary_search algorithm 
#
# Input:
# - a list of integers (a) on a line of STDIN with the first integer being the number of elements
# E.g.
# 5, 1, 5, 8, 12, 13, where n = 5 
# - second line, a list of integers (b) that are search items read from STDIN, with 
# 	the first integer being the number of elements
# E.g. 
# 5, 8, 1, 23, 1, 11, where k = 5 
#
# Output: 
# - the indexes of the searched item in the first list
# - return -1 for not found
# 
# Constraints: 
# 1 <= n,k <= 10**5
# element in the list: 1 <= element <= 10**9
# input is sorted for (a) 
# 
# Usage:
# python3 binary_search.py 
# 5 1 3 5 7 9 
# 5 0 3 4 7 8 
# -1 1 -1 3 -1 
#
# Testing:
# - unit test for this code can be found in: test_binary_search.py
# - Usage: python3 test_binary_search.py -v 
# 


def binary_search(searchList,item):
	#
	# Input: 
	# - searchList, a list of integer values that are sorted
	# - item, an integer to be search for in the list
	# E.g 
	#
	# Output:
	# - if item found in searchList:
	#	- the zero based index of item in searchList
	# - if item NOT found
	# 	- -1 (negative 1)
	#
	result = -1 

	debug = False

	# Code goes here 
	l = len(searchList)
	high = l - 1
	low = 0 
	
	while low <= high: 
		mid = low + (high - low)//2
		if debug: print(">>> low: " + str(low) + " mid: " + str(mid) + " high: " + str(high) )
		if item == searchList[mid]:
			return mid
		if item > searchList[mid]:
			low = mid + 1
		else:
			high = mid -1 

	return result

# 
# note: this snippet of code "linear_search" was provided as starter 
# code by the course creators - Coursera - Data Structures and algorithms 
# small modifications where my by me to adjust variables
# 
def linear_search(searchList, item):
    for i in range(len(searchList)):
        if searchList[i] == item:
            return i
    return -1

def doStuff(listOfElementsA, listOfElementsB):
	#
	# this is the "main" program driver rountine
	# 
	# Input:
	# - listOfElementsA: first sorted list of integers
	# - listOfElementsB: second sorted list of integers
	# - first element of each list n,k is the number of elements in the list
	#
	# Output:
	# - list containing the indexes of each searched item
	#

	resultSet = []

	# Code goes here

	# first elements are supplied in the assignment, not sure why needed
	# remove them
	del listOfElementsA[0]
	del listOfElementsB[0]

	for i in listOfElementsB:
		#r = linear_search(listOfElementsA, i)
		r = binary_search(listOfElementsA, i)
		resultSet.append(r)
	
	return resultSet

def displayOutput(res):
	#
	# Input:
	# - res -> is a list of integer values 
	# - Eg. [2, 12, 30]
	#
	# Output:
	# - output each integer value, all output on a single line
	# E.g.
	# 2 12 30 
	# 
	for i in res:
		print(str(i) + " ", end="")
	print()  

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

	# Get rest of input
	#
	inputDataA = getInput_list() 
	inputDataB = getInput_list()

	res = doStuff(inputDataA, inputDataB)
	displayOutput(res)

if __name__ == "__main__":

	runProgram() 
	
#
# End of file.
#
