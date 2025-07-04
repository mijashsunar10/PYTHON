a = (1,2,3,4,5)
print(type(a))

b=(1)
print(type(b))#this is not a tuple it is an integer

c = (1,)  # this is a tuple with one element
print(type(c))  # this is a tuple

d= (1, 2, 3, 4, 5)
d[0] = 10  # this will raise an error because tuples are immutable
print(d)


