## 延續上一支程式
# 先擷取特定例外並處理，最後再接收所有無法預期例外並處理
###############
def createFile(name):
    try:
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except FileNotFoundError:
        name = name.replace('/', '')
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except OSError:
        name = 'test_01'
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except:
        print('Unexpected Error!')

createFile('test/test1')
createFile('test?txt')
###############

###############
def add(x, y):
    try:
        s = x + y
    except TypeError:
        try:
            s = int(x) + int(y)
        except ValueError:
            print('ValueError!')
            return None
        except:
            print('Unexpected Error!')
            return None
    except:
        print('Unexpected Error!')
        return None

    return s

output = add(3, '5')
print(output)

output2 = add(3, 'a')
print(output2)
###############

