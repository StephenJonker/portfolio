#! /bin/bash 

# 
# Written by: Stephen Jonker
# Written on: Sunday 18 Feb 2018 
#
# Purose: 
# - Final bash shell programming challenge
# - HackerRank.com
#

MAXWIDTH=100	
MAXHEIGHT=63

###
#
# Functions go here
#
function build_board () {
	# 
	# this will build a board with a width of MAXWIDTH x MAXHEIGHT
	# it will be in a single dimension array of 6300 elements
	# it will be addressed via (x,y) coordianate pairs, converted to single dimension
	#
	board_index=1
	total_length=$(( $MAXWIDTH * $MAXHEIGHT ))
	while [ $board_index -le $total_length ]
	do
		board[${board_index}]=0	
		board_index=$(( ${board_index} + 1 ))
	done
}

function display_board () {
	# 
	# Display the contents of the board one line at a time
	# starting at the top
	# convert 0 chars to a underscore "-" 
	# convert 1 chars to a one "1", well that seem redundent, so just print it
	#
	x_index=1
	y_index=${MAXHEIGHT}
	while [ ${y_index} -ge 1 ]
	do
		while [ ${x_index} -le $MAXWIDTH ]
		do
			abs_index=$(( (${y_index} - 1) * ${MAXWIDTH} + ${x_index} ))  

			if [ ${board[${abs_index}]} == "0" ]
			then 
				printf "%s" "_" 
			else
				printf "%s" "1"
			fi

			x_index=$(( ${x_index} + 1 ))
		done
		y_index=$(( ${y_index} - 1 ))
		x_index=1
		printf "\n" 
	done
}

function plot_xy () {

	# Helper function, plot a "1" at the x,y coordinates on the board
	# converts from x, y co-ordinates into absolute index
	#

	x=$1
	y=$2

	pos=$(( (${y} - 1) * ${MAXWIDTH} + ${x} ))  
	board[${pos}]=1
}

function draw_y () {
	# Input: x-pos y-pos depth 
	# x-pos: x position on board to start drawing 
	# y-pos: y position on the board to start drawing 
	# depth: vertical height or depth of the "y" to draw
	#
	# Output: none, places output in the board array
	#
	
	x_start=$1
	y_start=$2
	depth=$3

	# Draw stem
	draw_cnt=1
	while [ "$draw_cnt" -le "$depth" ]
	do
		x=${x_start}	
		y=$(( ${y_start} + ${draw_cnt} - 1 )) 
		plot_xy ${x} ${y}
		draw_cnt=$(( ${draw_cnt} + 1 ))
	done
	
	# Draw branches
	x_start=${x_start}
	y_start=$(( ${y_start} + ${depth} - 1 ))
		
	draw_cnt=1
	while [ "$draw_cnt" -le "$depth" ]
	do
		rhs_x=$(( ${x_start} + ${draw_cnt} ))	
		rhs_y=$(( ${y_start} + ${draw_cnt} )) 
		plot_xy ${rhs_x} ${rhs_y}

		lhs_x=$(( ${x_start} - ${draw_cnt} ))	
		lhs_y=$(( ${y_start} + ${draw_cnt} )) 
		plot_xy ${lhs_x} ${lhs_y}

		draw_cnt=$(( ${draw_cnt} + 1 ))
	done

	next_depth=$(( ${depth} / 2 )) 
	
	# Adjust final y value to start next iteration correctly
	lhs_y=$(( ${lhs_y} + 1 ))
	rhs_y=$(( ${rhs_y} + 1 ))

	# Ok, so bash does not support returning arrays from functions!
	# so modifing "Global" array for this purpose
	# 
	result=( "${lhs_x}" "${lhs_y}" "${next_depth}" "${rhs_x}" "${rhs_y}" "${next_depth}" )
}

function dostuff () {
	if [ $# -eq 0 ] 
	then
		iterations=1
	else 	
		iterations=$1
	fi	

	end_value=( 16 8 4 2 1 0 ) 

	x=50	# initial x value
	y=1	# initial y value
	d=16	# initial depth

	r=($x $y $d) 
	k=0

	while [ "$k" -lt "${#r[@]}" ]
	do	
		offset1=$(( $k + 1 ))
		offset2=$(( $k + 2 ))
			
		x=${r[ $k ]}
		y=${r[ $offset1 ]}
		d=${r[ $offset2 ]}
		
		draw_y $x $y $d  

		# End condition
		ev="${end_value[${iterations}]}"	
		if [ "${result[2]}" -gt "${ev}" ] 
		then
			r2=( "${r[@]}" "${result[0]}" "${result[1]}" "${result[2]}" "${result[3]}" "${result[4]}" "${result[5]}")  
			r=( ${r2[@]} )
		fi

		k=$(( ${k} + 3 ))
	done
}

build_board 

result=()

read n
dostuff n

display_board

#
# EOF
#
