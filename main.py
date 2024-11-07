import os
def intro():
    user_input = input("Enter a file name: ")
    fd = open(user_input, "r")
    values = fd.readline()
    fd.close()
    return values
def seats(values):
    for name in values:
