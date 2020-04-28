## 除 try 和 except ，還有其他語法
# else 及 finally
def divide(x, y):
    print('x =', x, 'y =', y)
    try:
        result = x / y
    except ZeroDivisionError:
        print('不可除以0')
    except:
        print('無法預期的錯誤')
    else:
        print('答案是', result)
    finally:
        print('無論如何都會執行這段')
        print('==========')

divide(3, 2)
divide(3, 0)
divide(3,'a')
