#Write a program to find oute whether a given post is talking about "Harry" or not.

post = input("Enter the post: ")
if("Harry" in post):
    print("This post is about Harry")
else:
    print("This post is not about Harry")

dost = input("Enter the post: ")
if("Harry".lower() in dost.lower()):
    print("This post is about Harry")
else:
    print("This post is not about Harry")
