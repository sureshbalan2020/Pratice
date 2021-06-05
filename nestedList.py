menu= [
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","spam"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["egg","bread"],
]
for i in menu:
    for j in i:

        if j == "spam":
            break
      

for i in menu:
    if "spam" not in i:
        print(i)
