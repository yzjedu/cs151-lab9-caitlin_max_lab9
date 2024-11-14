# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

import os
* Purpose:  reads filename
* name: read_filename
* Parameters: none
* Return: f_name
* algorithm:.
  1. prompt user to input file name
  2. while file name does not exist
     1. output error message
     2. prompt user to input file name
  3. return f_name



* Purpose:  converts file data to a list
* Name: file_list
* Parameters: f_name
* Return: names
* algorithm:
  1.  set fd equal to open file name for reading
  2. set names equal to file data
  3. close file
  4. return names


* Purpose:  prints seat placement
* Name: seat_placement
* Parameters: names
* Return: none
* algorithm:
  1.  set table equal to 1
  2. set seat equal to 1
  3. for name in names
     1. print seat assignment
     2. seat += 1
     3. if seat is equal to 6
        1. table += 1
        2. seat is equal to 1


* Purpose:  runs main program
* Name: main
* Parameters: none
* Return:none
* algorithm:
  1.  call read file_name
  2. call file_list
  3. call seat_placement