#printing characters in astring
name = input("Enter your Names:")

#result=len(name)
#.find returns the first occurence of a given character. The position
#prints the last occurence.Incase the character appears twice"
result =name.rfind(" ")
print(result)