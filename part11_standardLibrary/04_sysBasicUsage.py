import sys

## 標準輸入
# 試著用標準輸入接收資料
print('What is your name?')
name = sys.stdin.readline()
print('Hello ', name)
# 與input()做比較
name = input('What is your name?\n')
print(name)


