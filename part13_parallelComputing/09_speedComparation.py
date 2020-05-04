import multiprocessing as mp
import threading
import os
import time

def longTime(i):
    print('PID: {}, Task: {} .'.format(os.getpid(), i))
    for i in range(0, 100000):
        print('PID: {}, Task: {} echo .'.format(os.getpid(), i))
        time.sleep(0.0001)
    # result = 10 ** 30
    # print('Result: {}'.format(result))

if __name__ == '__main__':
    N = 10

    start_time = time.time()

    print('===\nMULTIPROCESSING:\n===')

    print('母程序PID: {}'.format(os.getpid()))

    processes_list = list()
    for i in range(0, N):
        processes_list.append(mp.Process(target=longTime, args=(i,)))

    for i in range(0, N):
        processes_list[i].start()

    for i in range(0, N):
        processes_list[i].join()

    end_time = time.time()
    mpt = end_time - start_time
    print('總共花費 {} 秒'.format(mpt))

    print('\n=======================\n')

    start_time = time.time()

    print('===\nMULTITHREADING:\n===')

    print('母程序PID: {}'.format(os.getpid()))

    threads_list = list()
    for i in range(0, N):
        threads_list.append(threading.Thread(target=longTime, args=(i,)))

    for i in range(0, N):
        threads_list[i].start()

    for i in range(0, N):
        threads_list[i].join()

    end_time = time.time()
    mtt = end_time - start_time
    print('總共花費 {} 秒'.format(mtt))

    print()
    print()
    print('Multiprocessing\t{} sec.'.format(mpt))
    print('Multithreading\t{} sec.'.format(mtt))
