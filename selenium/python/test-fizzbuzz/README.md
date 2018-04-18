# Selenium FizzBuzz Javascript test using Python 

## This is Python Selenium WebDriver test of FizzBuzz written in HTML-CSS-Javascript

This is some Python code that will use Selenium WebDriver to do some basic tests of an HTML FizzBuzz program 

- launch Firefox via Python3, Selenium WebDriver
- open the HTML page by direct file access
- veriyf the page title is set correctly
- locate and trigger the output of the FizzBuzz program on the HTML page
- pause to observe output 
- close Firefox

### Note:

- Python3, Selenium WebDriver, Firefox and geckodriver are required
- The HTML-CSS-Javasript program being testing is purely front end, and does not need a webserver
- It runs just as files in the browser
- For this reason the full path to the index.html must be set in the python test driver script

### Usage: python3 ./test-fizzbuzz.py

## Description: program under test

- This is a version of FizzBuzz written in HTML-CSS-Javascript

- FizzBuzz is a programming exercise often given as a test during interviews for software developers
- The program is supposed to display the integer values of "N" between 1 and 100
- Except in the following cases...
	- if the value of N is evenly divisible by 3, then output N and the word "Fizz"
	- if the value of N is evenly divisible by 5, then output N and the word "Buzz"
	- and when N is divisible by 3 and 5, output N and "FizzBuzz"

## Eg.

- When n = 6, output "Fizz"
- When n = 10, output "Buzz"
- When n = 15, output "FizzBuzz"

