def printMax(x, y):
    '''Выводит максимальное из двух чисел.

       Оба значения должны быть целыми числами.'''
    x = int(x) # convert
    y = int(y)

    if x > y:
        print(x, 'bigger')
    else:
        print(y, 'bigger')

printMax(3, 5)
print(printMax.__doc__)