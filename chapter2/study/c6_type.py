#type function and type casting

a= 3
b=type(a)
print(b)

a= 3.2
b=type(a)
print(b)

a= "ANmol"
b=type(a)
print(b)

#we cab easily convert from number to string and string to number if possible
a="3.3"
b=float(a)
c=type(b)
print(c)

c="anmol"
b=int(c)
d=type(b)
print(d) #it is not possible cuz above is string so it is not possible to change into int
