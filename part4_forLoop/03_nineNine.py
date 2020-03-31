# 正常九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print('%3d X%3d =%3d || '%(i, j, i*j), end = '')
        if j == 9:
            print()

print()

# 只印出下三角形
for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print('%3d X%3d =%3d || ' % (i, j, i * j), end='')
        if j == 9:
            print()
