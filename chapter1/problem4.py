#Write a python program to print the contens of directort using th os module.Search online for the function which does that .
import os

# Print contents of the current directory
directory_path = '/'

contents = os.listdir(directory_path)

for item in contents:
    print(item)
