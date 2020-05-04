import time
import os

def longTime(i):
    print('PID: {}, Task: {} .'.format(os.getpid(), i))
    time.sleep(2)
    result = 10 ** 30
    print('Result: {}'.format(result))

if __name__ == '__main__':
    # 開始時間
    start_time = time.time()

    # 假設該任務需要執行 4 次
    for i in range(0,4):
        longTime(i)

    end_time = time.time()
    print('總共花費 {} 秒'.format(end_time - start_time))
