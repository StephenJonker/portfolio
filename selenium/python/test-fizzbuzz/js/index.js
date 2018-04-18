//
// Javascript template file
//

// Written by: Stephen Jonker
// Written on: Tuesday 13 Feb 2018 
// Copyright (c) 2018 Stephen Jonker - www.stephenjonker.com
//
// Purpose:
// Javascript functions for FizzBuzz 
//

function testIndexJS() {
	// testing function to log a message to the console when the html page has been loaded
	console.log("TEST: index.js - testIndexJS ");
}

function doFizzBuzz() {
	// 
	// Driver function for the FizzBuzz function
	// This function is called from the onClick event on the web page
	// - It handles the looping through values, formatting and dynamic updates to the DOM, for output
	// 
	// console.log("TEST: index.js - doFizzBuzz");

	var element = document.getElementById("output");

	var str1 = "";
	var str2 = "";

	var startValue = 1;
	var endValue = 100;

	for ( i = startValue; i <= endValue; i++) {
		str2 = FizzBuzz(i);	
		str1 = str1.concat(i," : ", str2, "<br>");
		element.innerHTML = str1;
	}
}

function FizzBuzz(n) {
	//
	// Given an integer value of n, return a fizzbuzz responce
	// - empty string, default 
	// - Fizz, n evenly divisible by 3 
	// - Buzz, n evenly divisible by 5 
	// - FizzBuzz, n evenly divisibile by 3 and 5 
	//

	// For testing and debugging
	// debug = true;
	debug = false; 

	var flag = 0; 
	if ( debug ) { console.log("n=",n); }
	if ( n % 3 == 0) {
		flag = flag + 1;
		if (debug) { console.log("Fizz"); }
	}
	if ( n % 5 == 0 ) {
		flag = flag + 2; 
		if ( debug ) { console.log("Buzz"); }
	}

	switch ( flag ) {
		case 0:
			res = "";
			break;
		case 1: 
			res = "Fizz";
			break;
		case 2: 
			res = "Buzz";
			break;
		case 3: 
			res = "FizzBuzz";
			break;
		default:
			res = "ERROR: something went wrong!";
	}
	if (debug ) { console.log("RES = ",res); }
	return res;
}
