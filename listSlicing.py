list1=[6,2,3,4,5,6,[4,5],8]
#using remove deleting the elements from list
#remove() deletes the first instance of a value in a list. This method should be used when one knows exactly which value they want to delete regardless of the index. The code below demonstrates this:

list1.remove(6)
print(list1)
#del can be used to delete a single index of a list, a slice of a list, or the complete list. For this shot, let’s look at how we can delete a value at a certain index with the del keyword:

del list1[6]
print(list1)
del list1[2:]
print(list1)

#The pop method removes an element at a given index and returns its value. The code below shows an example of this:

list1.pop(1)
print(list1)