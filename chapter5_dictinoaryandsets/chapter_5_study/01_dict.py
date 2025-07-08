a = {
    "Hari" : 100,
    "Sita" : 200,
    "Ram" : 300,
    "Gita" : 400,
    "Ram" : 500,  # This will overwrite the previous "Ram" entry
}

print(a, type(a))

# print(a[0])#tHIS WILL RAISE AN ERROR BECAUSE DICTIONARY DOES NOT SUPPORT INDEXING
print(a["Sita"]) # This will print the value associated with the key "Sita"