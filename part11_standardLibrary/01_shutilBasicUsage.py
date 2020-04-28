import shutil

## 先創建目錄及檔案再進行shutil檔案操作
import os
path1 = 'test/'
path2 = 'test1/test2/'
tmpfile = 'test.txt'
if not os.path.exists(path1) or not os.path.exists(path2):
    os.mkdir(path1)
    os.makedirs(path2)
with open(path1 + tmpfile, 'w') as f:
    f.write('123')

## 移動文件或目錄
# 使用move()將 test/test.txt 移動到 test1/test2/ 目錄下
path1 = 'test/'
path2 = 'test1/test2/'
tmpfile = 'test.txt'
shutil.move(path1 + tmpfile, path2 + tmpfile)
# 再將 test2 目錄整個搬到 test/ 裡面
shutil.move('test1/test2', 'test/')

## 複製檔案
# 將 test/test2/test.txt 這個文件複製到 test1/
shutil.copy('test/test2/test.txt', 'test1/')
# shutil.copy('test/test2', 'test1/') # 因為 test2/ 目錄非空，會出現錯誤訊息

## 複製目錄
shutil.copytree('test/test2', './test1/test2')

## 刪除目錄
shutil.rmtree('test1')
shutil.rmtree('test')