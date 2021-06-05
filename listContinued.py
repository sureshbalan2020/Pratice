evenNumber = [2,4,6,8,10]
oddNumber = [1,3,5,7,9]
combinedList=evenNumber+oddNumber
print(combinedList)
print (sorted(combinedList))
print(combinedList)
newCombinedlist = list(combinedList)
#above statement creates a copy of existing list instead of sharing the same address
print (newCombinedlist)
print(newCombinedlist is combinedList)
print(newCombinedlist == combinedList)
combinedList.append(11)
print(combinedList)
print(newCombinedlist)
