#!/usr/bin/env bash

# First method that came up to my mind. Checks if the number of arguments is 0.
if [[ $# -eq 0 ]]
then
	echo "One for you, one for me."
else
	echo "One for $1, one for me."
fi

# Could also use ${1: -default} which means if variable $1 doesnt exists, it
# will use the variable default instead. So in this case that would been like
# echo "One for ${1:-"you"}, one for me."



