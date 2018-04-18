# uses python3
#
# Written by: Stephen Jonker
# Written on: Tuesday 26 Sept 2017
# Copyright (c) 2017 Stephen Jonker - www.stephenjonker.com
#
# Overview:
# - unittests for binary_search 
# - Data Structures and Algorithms 
# 
# Purpose: 
# - unittest for binary_search.py
# 
# Usage:
# 	python3 ./test_binary_search.py -v 
#

import unittest
import binary_search

class test_binary_search(unittest.TestCase):

	# unit test - doStuff
	#
	#@unittest.skip("Not ready yet")
	def test_bsearch_doStuff_1(self):
		a = [5, 1, 5, 8, 12, 13]
		b = [5, 8, 1, 23, 1, 11]
		expected_result = [2, 0, -1, 0, -1]
		self.assertEqual(binary_search.doStuff(a,b), expected_result)
	
	def test_bsearch_doStuff_2(self):
		a = [1, 4]
		b = [1, 4]
		expected_result = [0]
		self.assertEqual(binary_search.doStuff(a,b), expected_result)

	def test_bsearch_doStuff_3(self):
		a = [6, 4, 4, 4, 4, 4, 4]
		b = [6, 4, 4, 4, 4, 4, 4]
		expected_result = [2, 2, 2, 2, 2, 2]
		self.assertEqual(binary_search.doStuff(a,b), expected_result)

	def test_bsearch_doStuff_4(self):
		a = [6, 4, 4, 4, 4, 4, 4]
		b = [6, 5, 6, 7, 8, 8, 9]
		expected_result = [-1, -1, -1, -1, -1, -1]
		self.assertEqual(binary_search.doStuff(a,b), expected_result)
	
	def test_bsearch_doStuff_5(self):
		a = [10, 1, 1, 2, 3, 5, 8, 13, 21, 33, 54]
		b = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
		expected_result = [2, 3, -1, 4, -1, -1, 5, -1, -1, -1]
		self.assertEqual(binary_search.doStuff(a,b), expected_result)
	
	def test_bsearch_doStuff_6(self):
		a = [10, 1, 1, 2, 3, 5, 8, 13, 21, 33, 54, 87]
		b = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 90]
		expected_result = [2, 3, -1, 4, -1, -1, 5, -1, -1, -1, -1]
		self.assertEqual(binary_search.doStuff(a,b), expected_result)
	
	def test_bsearch_doStuff_7(self):
		a = [11, 1, 1, 2, 3, 5, 8, 13, 21, 33, 54, 87]
		b = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 87]
		expected_result = [2, 3, -1, 4, -1, -1, 5, -1, -1, -1, 10]
		self.assertEqual(binary_search.doStuff(a,b), expected_result)
	
	def test_bsearch_doStuff_8(self):
		a = [11, 1, 1, 2, 3, 5, 8, 13, 21, 33, 54, 87]
		b = [11, 1, 3, 4, 5, 1, 7, 8, 9, 10, 11, 87]
		expected_result = [0, 3, -1, 4, 0, -1, 5, -1, -1, -1, 10]
		self.assertEqual(binary_search.doStuff(a,b), expected_result)

	# unit test - linear_search
	#
	def test_bsearch_linear_search_1(self):
		a = [1, 5, 8, 12, 13]
		b = 8
		expected_result = 2
		self.assertEqual(binary_search.linear_search(a,b), expected_result)

	def test_bsearch_linear_search_2(self):
		a = [1, 5, 8, 12, 13]
		b = 1
		expected_result = 0
		self.assertEqual(binary_search.linear_search(a,b), expected_result)
	
	def test_bsearch_linear_search_3(self):
		a = [1, 5, 8, 12, 13]
		b = 23
		expected_result = -1
		self.assertEqual(binary_search.linear_search(a,b), expected_result)

	# unit test - linear_search
	#
	#@unittest.skip("Not ready yet")
	def test_bsearch_binary_search_1(self):
		a = [1, 5, 8, 12, 13]
		b = 8
		expected_result = 2
		self.assertEqual(binary_search.binary_search(a,b), expected_result)

	#@unittest.skip("Not ready yet")
	def test_bsearch_binary_search_2(self):
		a = [1, 5, 8, 12, 13]
		b = 1
		expected_result = 0
		self.assertEqual(binary_search.binary_search(a,b), expected_result)
	
	#@unittest.skip("Not ready yet")
	def test_bsearch_binary_search_3(self):
		a = [1, 5, 8, 12, 13]
		b = 23
		expected_result = -1
		self.assertEqual(binary_search.binary_search(a,b), expected_result)
	
if __name__ == "__main__":
	unittest.main()

#
# End of file.
# 
