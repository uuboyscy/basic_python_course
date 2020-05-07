import glob

# 秀出所有資料夾
print('所有資料夾：')
all_python_folder = glob.glob('../part1*')
for p in all_python_folder:
    print(p)

print('\n所有程式：')
# 秀出所有程式
all_python_file = glob.glob('../part1*/*.py')
for p in all_python_file:
    print(p)

# 路徑篩選
print('\n特定路徑：')
some_path = glob.glob('../part1[2-4]*/0[1-3]*')
for p in some_path:
    print(p)
