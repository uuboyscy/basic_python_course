# list 基本操作
test_list = [1, 2, 3, 4, 5]
print('test_list 為', test_list)
# list 中的元素編號從 0 開始
print('第 一 個元素為', test_list[0])
print('第 四 個元素為', test_list[3])
print()

# list 裡面的元素也可以是字串
test_list2 = ['apple', 'banana', 'cat']
print('test_list 為', test_list2)
print('第 一 個元素為', test_list2[0])
print('第 三 個元素為', test_list2[2])
print()
# 使用 for 回圈取出 list 的每一個元素
print('使用 for 回圈取出 list 的每個元素')
n = 1
for w in test_list2:
    print('第 %s 個元素為'%(n), w)
    n += 1
print()

# list 中每個元素可以為不同型別，但不建議這樣做
nonproper_list = ['apple', 'banana', 'cat', 5]
for i in nonproper_list:
    print(type(i))
