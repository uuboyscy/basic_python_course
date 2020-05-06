import multiprocessing as mp
import threading
import os
import time
import psutil


def longTime(i):
    print('PID: {}, Task: {} .'.format(os.getpid(), i))
    for i in range(0, 1000000):
        print('PID: {}, Task: {} echo .'.format(os.getpid(), i))

if __name__ == '__main__':
    N = 4
    ppct = []
    tpct = []

    start_time = time.time()

    print('===\nMULTIPROCESSING:\n===')

    print('母程序PID: {}'.format(os.getpid()))

    processes_list = list()
    for i in range(0, N):
        processes_list.append(mp.Process(target=longTime, args=(i,)))

    for i in range(0, N):
        processes_list[i].start()

    for i in range(0, N):
        ppct.append(psutil.cpu_percent())
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
        tpct.append(psutil.cpu_percent())
        threads_list[i].join()

    end_time = time.time()
    mtt = end_time - start_time
    print('總共花費 {} 秒'.format(mtt))

    print()
    print()
    print('Multiprocessing\t{} sec.'.format(mpt))
    print('CPU usage: {} %'.format(sum(ppct) / len(ppct)))
    print()
    print('Multithreading\t{} sec.'.format(mtt))
    print('CPU usage: {} %'.format(sum(tpct) / len(tpct)))

