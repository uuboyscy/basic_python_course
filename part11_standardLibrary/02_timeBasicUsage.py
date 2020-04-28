import time

unix_sec = time.time()
loc_time = time.localtime()
utc_time = time.gmtime()
readable_time = time.asctime()

print('UNIX Time:', unix_sec)
print('本地時間為:', loc_time)
print('世界標準時間為:', utc_time)
print('本地時間可讀化:', readable_time)

## 時間日期格式化範例
loc_time_str = time.strftime('年份:%Y, 時間:%X', loc_time)
utc_time_str = time.strftime('現在UTC時間為今年第 %j 天, %c', utc_time)
print(loc_time_str)
print(utc_time_str)
