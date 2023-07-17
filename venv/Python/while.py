number = 23
running = True

while running:
    guess = int(input('Введите целое число : '))

    if guess == number:
        print('Your win')
        running = True
    elif guess < number:
        print('retorn biger number')
    else:
        print('return small num')
else:
    print('While exite.')

print('Bye')