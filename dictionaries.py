sampleDict = {"name": "Raj",
              "age": "31",
              "gender" : "M" ,
              "Date_of_birth": "01/01/2001"
        }
print(sampleDict)
print(sampleDict["name"])
for i in sampleDict:
    print(i)
    print(sampleDict[i])
print ("-"*40)
for i in sampleDict.keys():
    print(i)

print ("-"*40)
for i,j in sampleDict.items():
    print(i+"-"+j)

print ("-"*40)

sampleDict["address"] = "Delhi India"

print(sampleDict["address"])
sampleDict["name"]= "Arjun"
print(sampleDict["name"])
print(sampleDict)
print("*"* 40)
ordered_keys = list(sampleDict.keys())
ordered_keys.sort()
print(ordered_keys)

