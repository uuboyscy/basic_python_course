## 除 try 和 except ，還有其他語法
# else 及 finally
def divide(x, y):
    print('x =', x, 'y =', y)
    if not (type(x) in [type(1), type(1.1)] and type(y) in [type(1), type(1.1)]):
        raise TypeError('X and Y should be float or int.')
    elif y == 0:
        raise ZeroDivisionError('Y should not be zero.')
    else:
        return x / y

divide(3, 2)
divide(3, 0)
divide(3,'a')
