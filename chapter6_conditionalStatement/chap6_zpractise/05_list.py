#Write a program which finds out whethe a given name is present in alist or not.

names = ["Anmol", "Kiran", "Sita", "Ram"]
name = input("Enter the name to search: ")
if(name in names):
    print(f"{name} is in list")
else:
    print(f"{name} is not in list")