tmp_list = ['cat', 'dog', 'bear']

# 使用 append() 在 list 中加入新的元素
tmp_list = ['cat', 'dog', 'bear']
print('原list', tmp_list)
tmp_list.append('bird')
print('append後', tmp_list)

print()

# 使用 insert() 在 list 中加入新的元素
tmp_list = ['cat', 'dog', 'bear']
print('原list', tmp_list)
tmp_list.insert(2, 'cow')
print('insert後', tmp_list)

print()

# 使用 remove() 在 list 中加移除特定元素
tmp_list = ['cat', 'dog', 'bear']
print('原list', tmp_list)
tmp_list.remove('dog')
print('remove後', tmp_list)
