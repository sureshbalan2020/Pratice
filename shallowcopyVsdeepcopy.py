import copy
list1 = [1,2,3,4,5,[4,5]]
#how to shallowcopy
#A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original.
# The copying process does not recurse and therefore won’t create copies of the child objects themselves.
# In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.
# In python, this is implemented using “copy()” function.
# original elements of list

list2 = copy.copy(list1)
#how to use deepcopy
list3 = copy.deepcopy(list1)

print('original elements before sallowcopy and deepcopy')
for i in list1:
    print(i)

print(list2[5])
print(list2[5][1])
#changing elements of list2
list2[5][0]=8

print('original elements after sallowcopy and before deepcopy')
for i in list1:
    print(i)

list3[5][1]=10
print('original elements  after deepcopy')
for i in list1:
    print(i)
