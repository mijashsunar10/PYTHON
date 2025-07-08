#A spam commment is defined as a text containing following keywords:
#"make a lot of money", "buy now", "click this", "subscribe this", "click here".Write a program to detect whether a comment is spam or not. If it is spam, print "This is a spam comment" otherwise print "This is not a spam comment".

p1 = "make a lot of money"
p2 = "buy now"
p3 = "click this"
p4 = "subscribe this"
p5 = "click here"   
a = input("Enter the comment: ")

if((p1 in a) or (p2 in a) or (p3 in a) or (p4 in a) or (p5 in a)):
    print("This is a spam comment")
else:
    print(a)
