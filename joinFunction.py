mystring = '234,345,456,123,789'
mystrngaftersplit = mystring.split(',')
print(mystring)
print(mystrngaftersplit)
for i in mystrngaftersplit:
    print(i)


print("".join(mystrngaftersplit))

