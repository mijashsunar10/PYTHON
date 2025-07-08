#Write a program to find wheteher a given username contains less than 10 characters or not.

a = input("Enter your username: ")
if(len(a)<10):
    print("Username is less than 10 characters")
else:
    print("Username is greater than or equal to 10 characters")