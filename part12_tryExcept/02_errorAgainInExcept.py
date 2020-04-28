## 延續上一支程式
# 以下程式碼會在except的區塊內再次出錯
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
createFile('test?txt')
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

output2 = add(3, 'a')
print(output2)
###############
