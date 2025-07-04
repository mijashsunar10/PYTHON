#List are the container to store the set of values at any data type

friends = ["anmol", "mijash", 0 , 2, True, "hello", 3.4 ]
print(friends)
print(friends[0])  # Accessing the first element
print(friends[2])  # Accessing the second element
print(friends[3])  # Accessing the third element
print(friends[4])  # Accessing the fourth element
print(friends[5])  # Accessing the fifth element

#String cannot be changed but list are mutable
friends[0] = "Anmol"
print(friends[0])  # Now it will print "Anmol" instead of "

print(friends[1:4]) #:in the list 

