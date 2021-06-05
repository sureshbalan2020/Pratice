shoppingList =[]
choice = "-"
while choice != '0':
    if choice in "123456":
        print('adding item: {} in shoppingCart'.format(choice))
        if choice == '1':
            shoppingList.append('computer')
        elif choice == '2':
            shoppingList.append('mouse')
        elif choice == '3':
            shoppingList.append('keyboard')
        elif choice == '1=4':
            shoppingList.append('screen')
        elif choice == '5':
            shoppingList.append('HDMI cable')
        elif choice == '6':
            shoppingList.append('USB')
    else:
        print('please add the items from below')
        print('1:computer')
        print('2:mouse')
        print('3:keyboard')
        print('4:screen')
        print('5:HDMI cable')
        print('6:USB')
    choice = input()
print(shoppingList)

print ("*" *800)
print ("Example Finish")
print ("*" *800)

shoppingList =[]
avaiableItems=['computer','mouse','keyboard','screen','HDMI cable','USB']
choice = "-"
validChoices = [str(i) for i in range(1,len(avaiableItems)+1)]
#print(validChoices)
#print(str(1)) for i in range(1,len(avaiableItems)+1)



while choice != '0':
    if choice in validChoices:
        print('adding item: {} in shoppingCart'.format(choice))
        index = int(choice) - 1
        chosen_part = avaiableItems[index]
        shoppingList.append(chosen_part)
        # if choice == '1':
        #     shoppingList.append('computer')
        # elif choice == '2':
        #     shoppingList.append('mouse')
        # elif choice == '3':
        #     shoppingList.append('keyboard')
        # elif choice == '1=4':
        #     shoppingList.append('screen')
        # elif choice == '5':
        #     shoppingList.append('HDMI cable')
        # elif choice == '6':
        #     shoppingList.append('USB')
    else:
        print('please add the items from below')
        # for items in avaiableItems:
        #     print('{0}:{1}'.format(avaiableItems.index(items)+1,items))

        for number, items in enumerate(avaiableItems):
            print('{0}:{1}'.format(number + 1, items))
        # #enumerate(iterable, start=0)
        #
        # Parameters:
        # Iterable: any object that supports iteration
        # Start: the index value from which the counter is
        #               to be started, by default it is 0
    choice = input()
print(shoppingList)


print ("*" *800)
print ("Example optimization in list Finish")
print ("*" *800)

shoppingList =[]
avaiableItems=['computer','mouse','keyboard','screen','HDMI cable','USB']
choice = "-"
validChoices = [str(i) for i in range(1,len(avaiableItems)+1)]
while choice != '0':
    if choice in validChoices:
        print('adding item: {} in shoppingCart'.format(choice))
        index = int(choice) - 1
        chosen_part = avaiableItems[index]
        if chosen_part in shoppingList:
            shoppingList.remove(chosen_part)
            #This above statement removes the item from the shopping list#
        shoppingList.append(chosen_part)
    else:
        print('please add the items from below')

        for number, items in enumerate(avaiableItems):
            print('{0}:{1}'.format(number + 1, items))
    choice = input()
print(shoppingList)
