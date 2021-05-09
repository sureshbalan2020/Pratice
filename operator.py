#operator precedence
#PEMDAS (Parenthisis, exponents , multiplication/division, addition/substraction
#BEDMAS (brackets, exponents , division/mulitplication, addition/substraction
#BODMAS (brackets, order , division/mulitplication, addition/substraction
#BIDMAS (brackets, index , division/mulitplication, addition/substraction


a=12
b=3
print(a//b)
print(a%b)
print(b**2)
print(b**3)
print(a+b/3-4*12)
print(a+(b/3)-(4*12))
counter=1
if (a==12):
    counter=counter + 1
    counter -=5
    print("values are equal"+str(counter))

else:
    print("values are not equal")