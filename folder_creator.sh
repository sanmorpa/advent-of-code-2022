#!/bin/bash

# Script that creates a folder with the day, gets de AoC input and creates a python file with basic data ingestion

PURPLE='\033[0;35m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

python3 -c "import aocd"

if [ $(echo $?) -gt 0 ]
then

	printf "${YELLOW}WARNING. You don't have advent-of-code-data python package installed. ${NC}\n"
	printf "Would you like to install it now? (Y/N)\n>> "
	read ANSWER
	while [ "$ANSWER" != "Y" ] && [ "$ANSWER" != "y" ] && [ "$ANSWER" != "N" ] && [ "$ANSWER" != "n" ]
	do
	printf "Answer must be Y (Yes) or N (No)\n>> "
		read ANSWER
	done
	if [ "$ANSWER" == "Y" ] || [ "$ANSWER" == "y" ]
	then
		pip install advent-of-code-data
	elif [ "$ANSWER" == "N" ] || [ "$ANSWER" == "n" ]
	then
		printf "${RED}ERROR. Unable to proceed because 'advent-of-code-data' python packaged is not installed ${NC}"
		exit 0
	fi
fi

if [[ -z "${AOC_SESSION}" ]]
then
	printf "${PURPLE}You don't have set the AOC_SESSION env variable set. Please, intoduce it now. If you don't know how to do it, follow this tutorial: https://github.com/wimglenn/advent-of-code-wim/issues/1${NC}\n"
	echo -n ">> "
	read ID
	export AOC_SESSION=${ID}
	printf "${YELLOW}WANING. This has stored the ID ephimerally, if you want a more persistent storage, set it as an env variable or in the file ~/.config/aocd/token ${NC}\n"
fi

day=$(date +%d)
name="./day${day}"

mkdir ${name}
aocd > "${name}/input.txt"
touch "${name}/answer.py"
echo "# Data ingestion and processing" >> "${name}/answer.py"
echo "with open('${name}/input.txt') as file:" >> "${name}/answer.py"
echo "	lines = [line.rstrip() for line in file]" >> "${name}/answer.py"
