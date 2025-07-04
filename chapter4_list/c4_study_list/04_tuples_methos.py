a = (1,2,3,4,5,1)
print(type(a))  # <class 'tuple'>
c = a.count(1)  # count the number of occurrences of 1 in the tuple
print(c)  # 1
d = a.index(1)  # find the index of the first occurrence of 1 in the tuple
print(d)  # 0
e = len(a)  # get the length of the tuple
print(e)  # 6