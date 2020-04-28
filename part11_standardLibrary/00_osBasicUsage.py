import os

## 取得當前工作目錄
print('當前工作目錄為：', os.getcwd())

## 列出path目錄下有哪些檔案
path = './'
flist = os.listdir(path)
print('%s 目錄下存在的檔案有：'%(path), flist)

## 創建資料夾
path_one_dir = './test'
path_multi_dirs = './test1/test2'
# os.path.exists()檢查該目錄是否存在，若不存在，則創建目錄
if not os.path.exists(path_one_dir):
    # 利用os.mkdir()創建目錄
    os.mkdir(path_one_dir) # 在當前目錄創立一個資料夾
if not os.path.exists(path_multi_dirs):
    # os.mkdir(path_multi_dirs) # 若使用mkdir()創立多層資料夾，會出現錯誤訊息
    os.makedirs(path_multi_dirs) # 使用makedirs()則可成功創建多層目錄

## 改名
path_one_dir_old = './test'
path_multi_dirs_old = './test1/test2'
path_one_dir_new = './test_new'
path_multi_dirs_new = './test1_new/test2_new'
# 使用rename()可將單一目錄改名
os.rename(path_one_dir_old, path_one_dir_new)
# os.rename(path_multi_dirs_old, path_multi_dirs_new) # 若使用rename()修改多層目錄則出錯
# 使用renames()就可以一次修改多層目錄名稱
os.renames(path_multi_dirs_old, path_multi_dirs_new)
# 最後再將名稱改回來
os.rename(path_one_dir_new, path_one_dir_old)
os.renames(path_multi_dirs_new, path_multi_dirs_old)

## 刪除檔案
path_one_dir = './test'
# os.remove(path_one_dir) # remove()只可用來刪除檔案，若用來刪除資料夾會出現錯誤訊息
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('test')
os.remove('test.txt')

## 刪除資料夾
path_one_dir = './test'
path_multi_dirs = './test1/test2'
# 用rmdir()刪除一個空的資料夾
os.rmdir(path_one_dir)
# os.rmdir('./test1') # 因test1資料夾裡面有東西，所以會出現錯誤訊息
os.removedirs(path_multi_dirs) # 使用removedirs()則可以將test1連同裡面的東西一起刪除

