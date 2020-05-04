import multiprocessing as mp
import os
import time

def longTime(i):
    print('PID: {}, Task: {} .'.format(os.getpid(), i))
    time.sleep(2)
    result = 10 ** 30
    print('Result: {}'.format(result))

if __name__ == '__main__':
    start_time = time.time()
    print('母程序PID: {}'.format(os.getpid()))

    work1 = mp.Process(target=longTime, args=(1,))
    work2 = mp.Process(target=longTime, args=(2,))
    work3 = mp.Process(target=longTime, args=(3,))
    work4 = mp.Process(target=longTime, args=(4,))

    work1.start()
    work2.start()
    work3.start()
    work4.start()

    work1.join()
    work2.join()
    work3.join()
    work4.join()

    end_time = time.time()
    print('總共花費 {} 秒'.format(end_time - start_time))
