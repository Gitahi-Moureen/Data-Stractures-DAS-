myNames = ("Mary","Wanjiku","Chepkirui","Oleseiyan","Auma")

#Accessing an element in a tuple
print(myNames[3])

#Adding an element in a tuple
print(myNames)
myNames2 =list(myNames)
print(myNames2)
myNames2.append("Ivy")
print(myNames2)
myNames3 = tuple(myNames2)
print(myNames3)

#Removing an element in a tuple
myNames4 = list(myNames3)
print(myNames4)
myNames4.pop()
print(myNames4)
myNames5 = tuple(myNames4)
print(myNames5)