from string import ascii_lowercase as letters

rotters = letters[13:] + letters[:13]
newTEXT = ""
text = input("enter some text")
for each in text:
    currChar = letters.find(each)
    currChar = rotters[currChar]
    newTEXT = newTEXT + currChar
print(newTEXT)

