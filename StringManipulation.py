import operator


Str = "Hello I am a small string and i have less than 30 words"

print(f"Printing the String:\n\n{Str}")

Length = len(Str)

print(f" \n1. Length of the string is : {Length}\n")


#Manupulation of Index in a String
print("2. Index  Char")
for i,j in enumerate(Str):
    print(i,"\t\t",j)

Set = set(Str)
print("\n3. Frequency of each Character in the String using Set : ")

#Frequency of each character in String Method - 1
for i in Set:
    print(i, ":", Str.count(i))

print("\n4. Frequency of each Character in the String using Dict : ")
#Frequency of each character in String Method - 2
Dict = {}
for i in Str:
    Dict[i]=Str.count(i)
print(Dict)

print(max(Dict.items(), key=operator.itemgetter(1))[0])

print('''5.  Str.find('i') : ''', Str.find('i')) #Finding the index of the string

print('''6. Str.index("am") : ''', Str.index("am")) #Index of substring

print("7. Reverse String \n")
print(Str[::-1])

#Spliting into Spaces
l = Str.split(" ")
print("8. Spliting a String" , l)

print("\n9. Strings Starts and Ends with use : ")
print(Str.startswith("H")) #True
print(Str.endswith("i")) #false

print("\n10. Count a character l is : ", Str.count("l"))

#Replacing a particular substring
print("\n11. Replacing a Substring in a String :")
Replaced = Str.replace("Hello", "Hey !")
print(Replaced)

print("\n12. Uppercase : ", Str.upper(), "\n13. Lower : ", Str.lower(), "\n14. Alternatecase : ", Str.swapcase())


word = "    .Thank you        "
print("\n15. WORD :", word, "\nStrip  :",word.strip(),"\nlStrip :", word.lstrip(),"\nrStrip :",word.rstrip())

print("\n16. Concatenation", Str+word.strip())


print("\n17. Joining with a Separator : ", ("-".join(word)))
