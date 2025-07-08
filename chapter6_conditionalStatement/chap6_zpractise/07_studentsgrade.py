#Write a porgram to calculate the grade of a student from his marks from the following scheme:

# 1. 90-100 = A+
# 2. 80-89 = A
# 3. 70-79 = B+
# 4. 60-69 = B
# 5. 50-59 = C+
# 6. 40-49 = C
# 7. 33-39 = D
# 8. 0-32 = F

marks = int(input("Enter the marks of the student: "))
if 90 <= marks <= 100:
    print("Grade: A+")
elif(marks<=80 and marks>=80):
    print("Grade: A")
elif(70<= marks <=80):
    print("Grade: B+")
elif(60 <= marks < 70):
    print("Grade: B")
elif(50 <= marks < 60):
    print("Grade: C+")
elif(40 <= marks < 50):
    print("Grade: C")
elif(33 <= marks < 40):
    print("Grade: D")
else:
    print("Grade: F")

