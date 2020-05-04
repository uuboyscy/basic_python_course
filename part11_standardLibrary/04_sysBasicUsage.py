import sys

## 標準串流
# 試著用標準輸入接收資料
print('What is your name?')
name = sys.stdin.readline()
print('Hello ', name)
# 與input()做比較
name = input('What is your name?\n')
print(name)

# 使用標準輸出將資料輸出
sys.stdout.write('This is a book.')
sys.stdout.write('sys.stdout.write 預設不換行')
# 與print()比較
print('This is a book.')
print('print() 預設有換行')

# 使用標準輸出將錯誤訊息輸出
sys.stderr = open('testStdErr.txt', 'w')
# print(['1', '2'][2])

# 透過sys.path秀出引入模組時會用到的路徑
syspath = sys.path
print('syspath 為 ', type(syspath), ' 型別')
for path in syspath:
    print(path)

# sys.argv 參考 part10_inputOutput/02_sysArgv.py

# sys.platform 秀出作業系統資訊
print('作業系統相關資訊:')
print(sys.platform)

# sys.exit() 將會退出程序
sys.stderr = sys.__stderr__
sys.exit('退出程序後會印出此訊息')
