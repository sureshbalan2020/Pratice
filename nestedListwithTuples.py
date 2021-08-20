sampleList = [("egg","spam","bread"),
              ("egg","spam","butter"),
              ("bread", "spam", "butter"),
              ("bread", "jam", "butter")
                ]
for i in sampleList:
    item1,item2,item3 = i
    print(item1,item2,item3)

for item1, item2, item3 in sampleList:
    print (item1,item2,item3)

print(sampleList[0][2])
