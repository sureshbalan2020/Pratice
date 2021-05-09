string = 'abcdefg'
string1 = '9,223;272:036 854,123'
# for i in string:
#     print(i)
#     print(string.index(i))
seperator = ''
for i in string1:
    if not i.isnumeric():
        seperator = seperator + i
print(seperator)


for i in range(10):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(10,0,-2):
    print(i)


