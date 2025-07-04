#write a program to accpet marks of 6 studdents and display rhem in a sorted manner
# using list methods

students = []
a = int(input("Enter student 1 name: "))
students.append(a)
b = int(input("Enter student 2 name: "))
students.append(b)
c = int(input("Enter student 3 name: "))
students.append(c)
d = int(input("Enter student 4 name: "))
students.append(d)
e = int(input("Enter student 5 name: "))
students.append(e)
f = int(input("Enter student 6 name: "))
students.append(f)
d = sorted(students)
print(f"Students are {d}")
