import threading
import multiprocessing as mp
import os
import time

class Test:
    returned_value_list = list()

    def longTime(self, i):
        # print('PID: {}, Task: {} .'.format(os.getpid(), i))
        time.sleep(2)
        result = 10 ** 3
        # print('Result: {}'.format(result))
        self.returned_value_list.append(result)

if __name__ == '__main__':
    t_mp = Test()
    t_mt = Test()


    # Multiprocess
    mp_list = list()
    for i in range(0, 4):
        mp_list.append(mp.Process(target=t_mp.longTime, args=(i, )))

    for i in range(0, 4):
        mp_list[i].start()

    for i in range(0, 4):
        mp_list[i].join()
    print('Multiprocess data:', t_mp.returned_value_list)

    # Multithread
    mt_list = list()
    for i in range(0, 4):
        mt_list.append(threading.Thread(target=t_mt.longTime, args=(i,)))

    for i in range(0, 4):
        mt_list[i].start()

    for i in range(0, 4):
        mt_list[i].join()
    print('Multithread data: ', t_mt.returned_value_list)
