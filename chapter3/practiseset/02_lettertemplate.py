"""
Write a program to fill a letter template given below with name and date

"""

a = input("Enter a name")
b= input("Enter a date")
letter = f'''
Dear <|{a}\>,
You are selected
<|{b}\>'''
print(letter)

#this is the the porgram by beginer now for advance

letter1 = '''
Dear <|Name\>,
You are selected
<|Date\>
'''
c = letter1.replace('<|Name\>','Harry').replace('<|Date\>','12 september,2024')
print(c)



#NOw this is the advance method
#want more advance then

print(letter1.replace('<|Name\>',a).replace("<|Date\>",b))