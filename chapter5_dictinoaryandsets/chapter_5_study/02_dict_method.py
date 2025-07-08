marks = {
    "Harry" : 100,
    "Sita" : 200,
    0: 300,
}
# print(marks.items())

# print(marks.keys())

# print(marks.values())

# marks.update({"Harry": 400, "Sita": 500, "Rohan": 600})
# print(marks)

print(marks.get("Harry"))
print(marks["Harry"])#.This both give th same value and then if items doesnot exist then above one give none below one give error

print(marks.get("Harry1")) #this give none
print(marks["Harry1"]) #his give error


