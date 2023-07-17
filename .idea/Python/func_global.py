x = 50

def func():
    global x

    print('X Now ', x)
    x = 2
    print('And now X ', x)

func()
print('X = ',x)