# 三元運算子基本操作
# 若 n < 10 則讓 n 加 1
n = 9
print(n)
n += 1 if n < 10 else 0
print(n)
n += 1 if n < 10 else 0
print(n)

print()

a = 1
b = 2
# 將這個寫法改成三元運算子的寫法
if a > b:
    print('%s is larger than %s'%(a, b))
else:
    print('%s is not larger than %s'%(a, b))

print()

output_string = '' if a > b else 'not '
print('%s is %slarger than %s'%(a, output_string, b))