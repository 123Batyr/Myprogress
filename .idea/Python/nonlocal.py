def fun_outer():
    x = 2
    print('X = ',x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('and X = ',x)

fun_outer()