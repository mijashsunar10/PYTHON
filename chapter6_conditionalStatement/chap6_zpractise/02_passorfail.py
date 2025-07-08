#Write a program to find out whethe a student has passed or failed if it requires a totla of 40% and at least 33% in each subject to pass .Assume 3 subjects and take marks as an input from the user.

marks1 = int(input("Enter the marks of subject 1: "))
marks2 = int(input("Enter the marks of subject 2: "))
marks3 = int(input("Enter the marks of subject 3: "))
total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3
if(average_marks >=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed",average_marks)
else:
    print("You are failed",average_marks)

