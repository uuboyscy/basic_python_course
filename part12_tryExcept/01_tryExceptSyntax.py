## 直接用上一隻程式來修改
###############
def createFile(name):
    try:
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except:
        name = name.replace('/', '')
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')

createFile('test/test1')
###############

###############
def add(x, y):
    try:
        s = x + y
    except:
        s = int(x) + int(y)
    return s

output = add(3, '5')
print(output)
###############

