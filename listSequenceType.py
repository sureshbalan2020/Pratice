string="This is a string"
stringTo = string
print(stringTo, string)
print(id(stringTo), id(string))
string += "This string has changed"
print(stringTo, string)
print(id(stringTo), id(string))
print ("*" *800)
print ("Example immutable Finish")
print ("*" *800)
newList = [2,3,4,5,6]
newListChanged = newList
print(newList , newListChanged)
print(id(newList), id(newListChanged))
newList += [8]
print(newList , newListChanged)
print(id(newList), id(newListChanged))
a=b=c=d= newList
a.append(10)
print(c)
print(d)
print(newListChanged)
print ("*" *800)
print ("Example mutable Finish. List sets dictionary are example of mutable data types")
print ("*" *800)
#According to the source code, the maximum size of a list is PY_SSIZE_T_MAX/sizeof(PyObject*) . On a regular 32bit system, this is (4294967295 / 2) / 4 or 536870912. Therefore the maximum size of a python list on a 32 bit system is 536,870,912 elements.
for i in newList:
    print(i)

print ("*" *800)
print ("Example on iteration for list Finish")
print ("*" *800)

print(newList[4])
print(newList[1:3])

print ("*" *800)
print ("Example how to read elements of list using index")
print ("*" *800)

