s = {1, 2, 3 , "Harry"}
print(s, type(s))  # {1, 2, 3, 'Harry'}
s.add(4)
print(s)  # {1, 2, 3, 'Harry', 4
s.remove(3)
print(s)  # {1, 2, 'Harry', 4}
s.pop()  # removes and returns an arbitrary element
print(s)  # {2, 'Harry', 4} (the output may vary
