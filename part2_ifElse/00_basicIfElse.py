a = 1
b = 2

# if/else基本用法
if a > b:
    print('%s is larger than %s'%(a, b))
else:
    print('%s is not larger than %s'%(a, b))

# 加入elif
if a > b:
    print('%s is larger than %s'%(a, b))
elif a == b:
    print('%s is equal to %s'%(a, b))
else:
    print('%s is smaller than %s'%(a, b))
