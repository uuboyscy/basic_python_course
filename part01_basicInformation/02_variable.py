# 嘗試宣告變數
tmp_int1 = 10
tmp_int2 = 20

tmp_float1 = 1.5
tmp_float2 = 2.3

tmp_str1 = 'Hello world'
tmp_str2 = '12345'
tmp_str3 = '123.45'

# 將變數印出
print(tmp_int1)
print(tmp_float1)
print(tmp_str1)
print(tmp_str3)


'''
整數操作
'''
# 進制轉換
print('10 在十進位中為\t', 10)
print('10 在二進位中為\t', 0b10)
print('10 在八進位中為\t', 0o10)
print('10 在十六進位中為\t', 0x10)

# int()的使用
tmp_str2 = '12345'
tmp_float2 = 2.3
str_to_int = int(tmp_str2)
float_to_int = int(tmp_float2)
print(tmp_str2, '透過 int() 轉換變為', str_to_int)
print(tmp_float2, '透過 int() 轉換變為', float_to_int)
# int()此函式也可制定進制轉換的基數
tmp_bin = int('10', 2)
tmp_oct = int('10', 8)
tmp_hex = int('10', 16)
print('10 在二進位中為\t',tmp_bin)
print('10 在八進位中為\t', tmp_oct)
print('10 在十六進位中為\t', tmp_hex)

'''
浮點數操作
'''
# 浮點數的表示方式
print(1.0, '只要有小數點就會自動變成浮點數')
print(2.56473467846372865e11, '可用科學記號表示，e後面代表10的次方數')
print(1 + 1.0, '整數和浮點數會變成浮點數')
print(2.0 - 1.8, '浮點數會有精度問題出現')
# float()的使用
tmp_int1 = 10
tmp_str2 = '12345'
tmp_str3 = '123.45'
int_to_float = float(tmp_int1)
str_to_float2 = float(tmp_str2)
str_to_float3 = float(tmp_str3)
print(tmp_int1, '透過 int() 轉換變為', int_to_float)
print(tmp_str2, '透過 int() 轉換變為', str_to_float2)
print(tmp_str3, '透過 int() 轉換變為', str_to_float3)

'''
字串操作
'''
tmp_str1 = 'Hello world'
tmp_str2 = '12345'
tmp_str3 = '123.45'
# 字串與字串之間可用 + 做結合
con_str1 = tmp_str1 + tmp_str2
print(con_str1)
# 字串與數字不能直接相結合，須透過str()將數字轉為字串
con_str2 = tmp_str1 + str(10)
print(con_str2)
# 可使用[]將字串中的部分文字取出
print(tmp_str1[1]) # 印出e -> 編號從0開始
print(tmp_str1[0:3]) # 印出Hel，只印出0～2，第3個字不會印出
print(tmp_str1[:]) #  可將整個字串印出
print(tmp_str1[::2]) # 第三個數字可決定間隔
print(tmp_str1[-1::-1]) # 將字串反著印
# 字串「裡面的」函式
tmp_str1 = 'Hello world'
tmp_str2 = '12345'
tmp_str3 = '123.45'
split_str1 = tmp_str1.split()
print(split_str1) # split()預設用空格來分隔
split_str2 = tmp_str3.split('.')
print(split_str2) # split()可自行決定享用來分隔的字串
tmp_str3 = '123.45'
rep_str = tmp_str3.replace('.', '-')
print(rep_str)
# 大小寫轉換
tmp_str1 = 'Hello world'
upper_case_str = tmp_str1.upper()
print(upper_case_str)
lower_case_str = tmp_str1.lower()
print(lower_case_str)

