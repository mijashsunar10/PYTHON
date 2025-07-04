#Check that a type cannot be changed in python
a = (1, 2, 3)
a[1] = 4  # This will raise a TypeError because tuples are immutablepr
print(a)  # Uncommenting this line will show the tuple before the error