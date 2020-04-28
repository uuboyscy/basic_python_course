# 從 1 加到 n
n = 5
sum = 0
for i in range(1, n+1):
    sum += i
print('1 加到 %s 為 %s'%(n, sum))

# 從 1 乘到 n
sum = 1
for i in range(1, n+1):
    sum *= i
print('1 乘到 %s 為 %s'%(n, sum))
