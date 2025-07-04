#program to detec double space in the string

a = "hi  guys"
c = a.find("  ")
d = a.replace("  ", " ")
print(c)  # This will print the index of the double space
print(d)