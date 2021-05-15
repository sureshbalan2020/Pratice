shoppingCart = ['rice', 'sugar', 'soap', 'oil']
for i in shoppingCart:
    if i == 'soap':
        #exit()
        print('i dont want to buy')
    print('buy '+i)

for i in shoppingCart:
    for j in range(0,3):
        print(j)
        if i == 'soap':
            for k in range(0,4):
                print(i[k])
        print('i dont want to buy ')
    print('going to buy '+i)

for i in shoppingCart:
    if i == 'soap':
        continue
        print('i dont want to buy')
    print('buy'+i)

