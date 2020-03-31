n = 7
# 直角三角形
for i in range(1, n+1):
    print('*' * i)

print()

# 等腰三角形
for i in range(1, n+1):
    space_amount = -i + 7
    star_amount = 2*i - 1
    print(' ' * space_amount, '*' * star_amount)
