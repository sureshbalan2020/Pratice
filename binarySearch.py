import random
low = 1
high = 1000
answer = int(input('enter the number: '))
counter = 1
while True:
    print('\t guess in range of {} to {}'.format(low,high))
    guess = low + (high-low)//2
    high_low = input('computer guesses : {}, should i guess higher or lower ?'
                     'enter h,l,c'. format(guess)).casefold()
    if high_low == 'h':
        low = guess + 1
    elif high_low == 'l':
        high = guess - 1
    elif high_low == 'c':
        print('I got it in {} guesses'.format(counter))
        break
    else:
        print('enter only h,l,c')
    counter = counter + 1