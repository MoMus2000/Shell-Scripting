#!/bin/bash
echo "Script Excution Begins...."
echo "Enter your name and surname"  
echo "Name" $1
echo "Surname" $2
echo "Script name" $0

echo ""
echo ""

echo $*
echo $#
echo $@ 

echo ""
echo ""

#Print 2+2
val='expr 2 + 2' 
echo $val
echo ""
echo ""

a=15
b=20
if [ "$a" == "$b" ]
then 
echo "They are the same"
elif [ "$a" -lt "$b" ]
then
echo "a is smaller than b"
elif [ "$a" -gt "$b" ]
then
echo "a is greater than b"
else
echo "They are not the same"
fi

echo ""
echo ""

