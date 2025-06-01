'''String is inmutable
    Once a string is made then the characteer of string cannot be changed
    name = "Anmol"
    then in name all the string character has its index and index start from 0 
    a=0,n=1,m=2 and we can give index in negative also if we wawt 
    l=-1 o=-2 m=-3 like that

    string_slicing = name[index_start:index_end]
    index_start is included but index_end is not included

    '''

name = "anmol"
# nameshort = name[0:3] # Index 0,1 and 2 will be included but 3 will not be included
print('nameshort is:', name[0:3])
print("Display one character", name[1])
#print('nameshort is:', name[3:0]) THis will alson not work

# print("tHE NAME IS:", name[-2:-5]) THis wont work

print("tHE NAME IS:", name[-4:-2]) #this will work

#easiest way to find [-4:-2 ] is just make them opposite and -1

print("THen mae is ", name[1:3])

print("hello",name[:3]) #this means name[0:3]
print("the legth is ", name[1:]) # this mean 1:legth ie total length of the word