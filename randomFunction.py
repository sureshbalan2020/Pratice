import random
for i in range (1,11):
    print('random number {}'.format(random.randint(0,1000)))


low = 1
high = 1000
answer = random.randint(low,high)
guess = int(input('please guess your number: '))
while True:
    if guess == answer:
        print('you guessed it right ')
        break
    elif guess < answer:
        low = guess
        guess = int(input('As you guessed number smaller than calculated number, please enter the value between {} and {} '.format(low,high)))

    else:
        high = guess
        guess = int(input('As you guessed number larger than calculated number, please enter the value between {} and {} '.format(low,high)))