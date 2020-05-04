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

    processes_list = list()
    for i in range(0, 4):
        processes_list.append(mp.Process(target=longTime, args=(i,)))

    for i in range(0, 4):
        processes_list[i].start()

    for i in range(0, 4):
        processes_list[i].join()

    end_time = time.time()
    print('總共花費 {} 秒'.format(end_time - start_time))
