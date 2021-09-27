#!/bin/bash

echo "Type absolute path of folder to be openend"
read path
cd $path
count=0
for file in *
do
    echo $file
    ((count++))
done
echo "Total no. of contents in folder: " $path
echo $count