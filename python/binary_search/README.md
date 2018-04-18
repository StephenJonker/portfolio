# Binary_Search in Python3 

### Overview:
* binary_search 
* Data Structures and Algorithms 

### Purpose:
* write a binary_search algorithm 

### Input:
* a list of integers (a) on a line of STDIN with the first integer being the number of elements
* E.g.
* 5, 1, 5, 8, 12, 13, where n = 5 
* second line, a list of integers (b) that are search items read from STDIN, with 
the first integer being the number of elements
* E.g. 
* 5, 8, 1, 23, 1, 11, where k = 5 

### Output: 
* the indexes of the searched item in the first list
* return -1 for not found

### Constraints: 
* 1 <= n,k <= 10**5
* element in the list: 1 <= element <= 10**9
* input is sorted for (a) 

### Usage:
* python3 binary_search.py 
* 5 1 3 5 7 9 
* 5 0 3 4 7 8 
* -1 1 -1 3 -1 

### Testing:
* unit test for this code can be found in: test_binary_search.py
* Usage: python3 test_binary_search.py -v 

