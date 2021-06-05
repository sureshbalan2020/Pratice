evenNumber = [2,4,6,8,10]
oddNumber = [1,3,5,7,9]
print(evenNumber)
evenNumber.extend(oddNumber)
print(evenNumber)
#sorting
evenNumber.sort()
print(evenNumber)
#sorting in reverse
evenNumber.sort(reverse = True)
print(evenNumber)
#sum of all elements
print(sum(evenNumber))
print(min(evenNumber))
print(max(evenNumber))
a = '1231231231231465123'
print(a.count('1'))
a=[1,2,5,5,3,3,2,2,1,4,1,4,1,1,3,1,3,1,3,1,1]
print(a.count(3))
b=[str(i) for i in a]
print(b)
print(b.count('3'))

