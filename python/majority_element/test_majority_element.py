# uses python3
#
# Written by: Stephen Jonker
# Written on: Wednesday 27 Sept 2017
# Copyright (c) 2017 Stephen Jonker - www.stephenjonker.com
#
# Overview:
# - unittests for majority_element 
# - Data Structures and Algorithms 
# 
# Purpose: 
# - unittest for majority_element.py
# 
# Usage:
# 	python3 ./test_majority_element.py -v 
#

import unittest
import majority_element
import random

# Helper function - generate list of random test input of length(n)
def generator(n):
	#
	# Input: 
	# n - where n is the lenght of the list of random numbers
	# Output:
	# res - where res is a list of the randomly generated numbers 
	# 
	result = []
	for i in range(0,n):
		item = random.randint(1,10)
		result.append(item)

	return result

def generator2(n):
	#
	# Input: 
	# n - where n is the lenght of the list of random numbers
	# Output:
	# res - where res is a list of the randomly generated numbers 
	# 
	# Generate random data but 50% of the time add "3"
	# this should force a majority element of 3
	#
	result = [3]
	for i in range(0,n):
		item = random.randint(1,10)
		result.append(item)
		result.append(3)

	return result



class test_majority_element(unittest.TestCase):

	# unit test - doStuff
	#
	#@unittest.skip("Not ready yet")
	def test_me_doStuff_1(self):
		a = [1, 2, 3, 2, 2]
		expected_result = 1
		self.assertEqual(majority_element.doStuff(a), expected_result)
	
	def test_me_doStuff_1(self):
		a = [1, 2, 3, 5, 2]
		expected_result = 0
		self.assertEqual(majority_element.doStuff(a), expected_result)

	# unit test - majority_element_linear_search
	#
	#@unittest.skip("Not ready yet")
	def test_majority_element_linear_search_1(self):
		a = [1, 2, 3, 2, 2]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_linear_search(a), expected_result)

	def test_majority_element_linear_search_2(self):
		a = [5]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_linear_search(a), expected_result)

	def test_majority_element_linear_search_3(self):
		a = [1,2]
		expected_result = 0
		self.assertEqual(majority_element.majority_element_linear_search(a), expected_result)

	def test_majority_element_linear_search_4(self):
		a = [1,2,2]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_linear_search(a), expected_result)

	def test_majority_element_linear_search_5(self):
		a = [1,2,3]
		expected_result = 0
		self.assertEqual(majority_element.majority_element_linear_search(a), expected_result)

	def test_majority_element_linear_search_6(self):
		a = [1,2,3,4,5,8,8,8,8,8]
		expected_result = 0
		self.assertEqual(majority_element.majority_element_linear_search(a), expected_result)

	def test_majority_element_linear_search_7(self):
		# M.E. in second half
		a = [1,2,3,4,5,8,8,8,8,8,8]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_linear_search(a), expected_result)

	def test_majority_element_linear_search_8(self):
		# M.E. in first half
		a = [8,8,8,8,8,8,1,2,3,4,5]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_linear_search(a), expected_result)

	def test_majority_element_linear_search_9(self):
		# M.E. alternating
		a = [1,8,2,8,3,8,4,8,5,8,6,8]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_linear_search(a), expected_result)

	def test_majority_element_linear_search_9(self):
		# M.E. alternating reversed
		a = [8,1,8,2,8,3,8,4,8,5,8,6]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_linear_search(a), expected_result)

	def test_majority_element_linear_search_9(self):
		# M.E. longer 
		a = [8,1,8,2,8,3,8,4,8,5,8,6,7,7,7,7,7,8,8,8,8,8,8]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_linear_search(a), expected_result)

	def test_majority_element_linear_search_generator_1(self):
		# M.E. longer 
		a = generator(20)
		expected_result = 0
		self.assertEqual(majority_element.majority_element_linear_search(a), expected_result)

	def test_majority_element_linear_search_generator_2(self):
		# generated pseudo-random majority element 
		debug = False 

		count = 0
		numberOfTests = 1000
		listLength = 20 
		for loop in range(0,numberOfTests):
			if debug: print(">>> Generator 2: ", loop, " list length: ", listLength)
			a = generator2(listLength)
			expected_result = 1
			res = majority_element.majority_element_linear_search(a)
			count = count + res
			self.assertEqual(res, expected_result)
		
		self.assertEqual(count, numberOfTests)


	# unit test - majority element divide and conquer
	#
	#@unittest.skip("Not ready yet")

	def test_majority_element_divide_and_conquer_1(self):
		a = [1, 2, 3, 2, 2]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_divide_and_conquer(a), expected_result)

	def test_majority_element_divide_and_conquer_2(self):
		a = [5]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_divide_and_conquer(a), expected_result)

	def test_majority_element_divide_and_conquer_3(self):
		a = [1,2]
		expected_result = 0
		self.assertEqual(majority_element.majority_element_divide_and_conquer(a), expected_result)

	def test_majority_element_divide_and_conquer_4(self):
		a = [1,2,2]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_divide_and_conquer(a), expected_result)

	def test_majority_element_divide_and_conquer_5(self):
		a = [1,2,3]
		expected_result = 0
		self.assertEqual(majority_element.majority_element_divide_and_conquer(a), expected_result)

	def test_majority_element_divide_and_conquer_6(self):
		a = [1,2,3,4,5,8,8,8,8,8]
		expected_result = 0
		self.assertEqual(majority_element.majority_element_divide_and_conquer(a), expected_result)

	def test_majority_element_divide_and_conquer_7(self):
		# M.E. in second half
		a = [1,2,3,4,5,8,8,8,8,8,8]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_divide_and_conquer(a), expected_result)

	def test_majority_element_divide_and_conquer_8(self):
		# M.E. in first half
		a = [8,8,8,8,8,8,1,2,3,4,5]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_divide_and_conquer(a), expected_result)

	def test_majority_element_divide_and_conquer_9(self):
		# M.E. alternating
		a = [1,8,2,8,3,8,4,8,5,8,6,8]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_divide_and_conquer(a), expected_result)

	def test_majority_element_divide_and_conquer_9(self):
		# M.E. alternating reversed
		a = [8,1,8,2,8,3,8,4,8,5,8,6]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_divide_and_conquer(a), expected_result)

	def test_majority_element_divide_and_conquer_9(self):
		# M.E. longer 
		a = [8,1,8,2,8,3,8,4,8,5,8,6,7,7,7,7,7,8,8,8,8,8,8]
		expected_result = 1
		self.assertEqual(majority_element.majority_element_divide_and_conquer(a), expected_result)



	#@unittest.skip("Not ready yet")
	def test_majority_element_divide_and_conquer_generator_1(self):
		#
		# use data generator and compare results between 
		# M.E Linear Search & M.E. divide and conquer
		# 
		# This generator create random number, so the expect results should be no M.E. found 
		#
		debug = False

		count = 0  
		numberOfGeneratedTests = 1000 
		listLength = 1000
		for loop in range(0,numberOfGeneratedTests):
			if debug: print(">>> Generator: ", loop, " list length: ", listLength)
			a = generator(listLength)
			expected_result = majority_element.majority_element_linear_search(a)
			res = majority_element.majority_element_divide_and_conquer(a)
			count = count + res
			self.assertEqual(res, expected_result)

		self.assertNotEqual(count, numberOfGeneratedTests)
		self.assertEqual(count, 0)

	#@unittest.skip("Not ready yet")
	def test_majority_element_divide_and_conquer_generator_2(self):
		#
		# use data generator and compare results between 
		# M.E Linear Search & M.E. divide and conquer
		# 
		# This generator2 creates random number, but ensure that a M.E. exists
		# so the expect results should be M.E. found 
		#
		debug = False 

		count = 0
		numberOfGeneratedTests = 1000
		listLength = 1000
		for loop in range(0,numberOfGeneratedTests):
			if debug: print(">>> Generator 2: ", loop, " list length: ", listLength)
			a = generator2(listLength)
			expected_result = majority_element.majority_element_linear_search(a) 
			res = majority_element.majority_element_divide_and_conquer(a)
			count = count + res
			self.assertEqual(res, expected_result)
		
		self.assertEqual(count, numberOfGeneratedTests)


if __name__ == "__main__":
	unittest.main()

#
# End of file.
# 
