number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print('Поздравляю вы угадали,')
    print('(хотя и не выиграли никакого приза!)')
elif guess < number:
    print('нет загаданное число немног больше этого.')
else:
    print('нет загаданное число меньше этого.')

print('Stop')