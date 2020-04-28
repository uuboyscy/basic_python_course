'''
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''

## 直接將資料印出來
print('# 直接將資料印出來')
print(1)
print('Hello world!')

print()

## 將宣告的變數印出
print('# 將宣告的變數印出')
a = 1
b = 'Hello world!'
print(a, b)

print()

## 操作sep參數，sep預設為空白鍵
print('# 操作sep參數')
print('aaa', 'bbb', 'ccc', sep='|')

print()

## 操作end參數，end預設為換行
print('# 操作end參數')
print('aaa', end='')
print('bbb', end='')
print('ccc')
print('ddd', end='')

print()

## 操作file參數，file預設為sys.stdout，也就是下方的console畫面
print('# 操作file參數')
print('file=sys.stdout:', '123')
print('file=open("./test.txt")', '123', file=open("./test.txt", 'w'))

print()

## 操作flush參數，flush預設為False
import time
print('# 操作flush參數')

f = open("./test.txt", 'a')
# flush為預設值False時，檔案會在關閉時才將縮有資料寫入
# 每5秒鐘開啟test.txt觀察資料寫入的狀況
for i in range(0, 5):
    print('123', file=f)
    time.sleep(5)
f.close()

f = open("./test.txt", 'a')
# flush設定為True時，每次執行print()都會將資料寫入檔案
# 每5秒鐘開啟test.txt觀察資料寫入的狀況
for i in range(0, 5):
    print('456', file=f, flush=True)
    time.sleep(5)
f.close()
