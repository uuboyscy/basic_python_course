'''
試著印出1到10
'''

# 先宣告一個變數，並定義為1
num = 1
# 當變數num小於或等於10的時候，執行回圈內容
print('印出1~10')
while num <= 10:
    # 將num印出
    print(num)
    # 回圈結束前將num加1
    num = num + 1
'''
試著印出1到n
'''
print('印出1~n')
n = input('輸入數字n:')
n = int(n)
num = 1
while num <= n:
    print(num)
    num = num + 1