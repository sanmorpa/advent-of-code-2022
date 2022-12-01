#!/bin/bash

# Script that creates a folder for each day named "day[number_of_day]" and an "answer.py" file inside of each folder

i=1
name="./day"

while [ $i -lt 26 ]
do
	if [ $i -lt 10 ]
	then
		mkdir "${name}0${i}"
		touch "${name}0${i}/answer.py"
	else
		mkdir "${name}${i}"
		touch "${name}${i}/answer.py"
	fi
	let "i+=1"
done
