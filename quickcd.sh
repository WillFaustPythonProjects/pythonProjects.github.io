#!/bin/bash



# copy files from this mac to the network backup, mr rowe grades these
cp -r . Student/W/F/WFaust4047/ddccode2/finalproject  


echo -e .
echo -e  copying files, please check for errors
echo -e .
read -p "Press [Enter] key to continue"
# pause and wait for user to hit enter on keyboard


# line below checks the current folder
echo
echo $ThisDir
echo
echo Here are your git hub local files:
echo

echo
cd Documents/GitHub/spacexlander.github.io

ls -P -l 
# list the files  -l is longer details like date and time
echo