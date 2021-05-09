for i in range(0,12):
    #print(i)
    print("No. is {3} squared is {2} cube is {3}".format(i, i**2, i**3, i**4))


    # right alignment
for i in range(1, 13):
    print("No. is {0:2} squared is {1:3} cube is {2:4}".format(i, i ** 2, i ** 3))

    # left alignment
for i in range(1, 13):
    print("No. is {0:2} squared is {1:<3} cube is {2:<4}".format(i, i ** 2, i ** 3))

pi=22/7
print(pi)
print("pi is: {0}".format(pi))
print("pi is: {0:12}".format(pi))
print("pi is: {0:12f}".format(pi))
print("pi is: {0:12.12f}".format(pi))
print("pi is: {0:12.30f}".format(pi))
print("pi is: {0:35.12f}".format(pi))
print("pi is: {0:35.50f}".format(pi))
print("pi is: {0:35.55f}".format(pi))
print (len("{0:35.32f}".format(pi)))

