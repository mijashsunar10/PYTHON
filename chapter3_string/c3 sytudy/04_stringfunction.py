name = "Anmol"
print(len(name))
print(name.endswith("ol"))#it shows true
print(name.endswith("ola"))

print(name.startswith("an"))#the function is case sensitive
print(name.startswith("An"))

#print(name.capitalize("Anmol"))  this wont work
print(name.capitalize())#This will work but the only first letter is captitlazis


s = "hello worls"
index = s.find("worls")
# index = s.find("w") This will also work
index = s.find("world")
print(index)

# string .replace

s = "hello world"
a = s.replace("world", "Anmol")
print(a)