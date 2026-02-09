#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/9 21:39
Email : adamyue@163.com
'''
from threading import Lock, Thread, Condition
from typing import Any

task_lock = Lock()

def task(name: str):
    global task_lock
    for n in range(2):
        task_lock.acquire()
        print(f'{name} - round {n} - step 1\n', end='')
        print(f'{name} - round {n} - step 2\n', end='')
        print(f'{name} - round {n} - step 3\n', end='')
        task_lock.release()

t1 = Thread(target=task, args=('T1',))
t2 = Thread(target=task, args=('T2',))
t3 = Thread(target=task, args=('T3',))

t1.start()
t2.start()
t3.start()

class SafeQueue:
    def __init__(self, max: int):
        self.__item_list = list()
        self.size = max
        self.__item_lock = Condition()

    def put(self, item: Any):
        with self.__item_lock:
            while len(self.__item_list) >= self.size:
                self.__item_lock.wait()

            self.__item_list.insert(0, item)
            self.__item_lock.notify_all()

    def get(self):
        with self.__item_lock:
            while len(self.__item_list) == 0:
                self.__item_lock.wait()

            result = self.__item_list.pop()
            self.__item_lock.notify_all()
        return result
