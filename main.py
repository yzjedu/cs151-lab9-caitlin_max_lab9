import os
# Programmers:  Caitlin Burns Max Rice
# Course:  CS151, professor Zee
# Due Date: 11/14
# Lab Assignment:  9
# Problem Statement:  prints seating chart
# Data In: file names
# Data Out: seating chart
# Credits: read me file
# Input Files: isaacman, yalew, nweke

# Purpose:  reads filename.
# Parameters: none
# Return: f_name
def read_filename():
    f_name = input('Enter file name: ')
    while not os.path.isfile(f_name):
        print('Error')
        f_name = input('Enter file name: ')
    return f_name

# Purpose:  converts file data to list
# Parameters: f_name
# Return: names
def file_list(f_name):
    fd = open(f_name, 'r')
    names = fd.readlines()
    fd.close()
    return names

# Purpose: prints seat assignment
# Parameters: names
# Return: none
def seat_placement(names):
    table = 1
    seat = 1
    for name in names:

        print(f'table {table}, seat {seat}, {name}')
        print('~' * 70)
        seat += 1
        if seat == 6:
            table += 1
            seat = 1


# Purpose: runs main program
# Parameters: none
# Return: none
def main():
    f_name = read_filename()
    names = file_list(f_name)
    seat_placement(names)


main()
