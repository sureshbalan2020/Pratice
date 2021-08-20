debt= 'C:/POC/debt.txt'
f = open(debt, mode='a+')
lines= f.read(4)
print(lines)
lines= f.readline()
print(lines)
lines= f.readlines()
print(lines)
f.write('\nabc:200')
f.close()

with open(debt,'a+') as writer:
    for i in range(10):
        writer.write(str(i))



with open(debt,'r') as reader:
    print(reader.readlines())



