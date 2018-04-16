#! /bin/bash 
#
# Written by: Stephen Jonker
# Written on: Tuesday 13 Feb 2018
#
# Copyright (c) Stephen Jonker 2018 - www.stephenjonker.com
#
# Description:
# - FizzBuzz is a programming exercise often given as a test during interviews for 
#   software developers
# - The program is supposed to dislay the integer values of "N" between 1 and 100
# - Except in the following case
# - if the value of N is evenly divisible by 3, then output N and the word "Fizz"
# - if the value of N is evenly divisible by 5, then output N and the word "Buzz"
# - and when N is divisible by 3 and 5, output N and "FizzBuzz" 
# Eg. 
# When n = 6, output "Fizz"
# When n = 10, output "Buzz" 
# When n = 15, output "FizzBuzz"
#
# Usage:
# 	bash ./fizzbuzz.sh 
#
# Environment:
# - Mac: OS X El Capitan Version: 10.11.6
# - bash: GNU bash, version 3.2.57(1)-release (x86_64-apple-darwin15)
#

cnt=1

while [ "$cnt" -le 100 ] 
do
	# flag
	# use binary bit positions 1 and 2 to flag detection of fizz, buzz or fizzbuzz
	# decimal equivalents are used
	# BIN	DEC 	Value	
	# ---	---	-----
	# 00 	0	just the regular number
	# 01 	1	fizz
	# 10 	2	buzz
	# 11 	3	fizzbuzz 
	#
	
	fizzbuzzflag=0

	# Check if divisible by 3, and set flag
	#
	if [ $(( $cnt % 3 )) -eq 0 ] 
	then 
		fizzbuzzflag=$(( $fizzbuzzflag + 1))
	fi

	# Check if divisible by 5, and set flag 
	#
	if [ $(( $cnt % 5 )) -eq 0 ] 
	then 
		fizzbuzzflag=$(( $fizzbuzzflag + 2))
	fi

	case $fizzbuzzflag in
		0)	echo "$cnt";;
		1)	echo "$cnt : Fizz";;
		2)	echo "$cnt : Buzz";;
		3)	echo "$cnt : FizzBuzz";;
		*)	echo "Error: something bad happened, bad value is fizzbuzztotal";;
	esac

	# Increment the loop variable
	# 
	cnt=$(( $cnt + 1)) 
done

#
# End of file.
#
