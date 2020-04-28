## 以下兩段程式碼將出現錯誤訊息
# 試著解讀錯誤訊息
###############
def createFile(name):
    with open(name, 'w', encoding='utf-8') as f:
        f.write('123')

createFile('test/test1')
###############

###############
def add(x, y):
    s = x + y
    return s

output = add(3, '5')
print(output)
###############

