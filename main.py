# -*-coding:utf-8-*-
import threadpool
import time
import random


def sayhello(string):
    print("Hello ", string)
    time.sleep(2)


name_list = ['alpha', 'beta', 'sigma', 'Omega']
start_time = time.time()
pool = threadpool.ThreadPool(10)
requests = threadpool.makeRequests(sayhello, name_list)
[pool.putRequest(req) for req in requests]
pool.wait()
print('%d second' % (time.time() - start_time))


def worker_get(string):
    return "[" + str(string) + "]"


def print_result(request, result):
    print("the result is %s %r" % (request.requestID, result))


data = [random.randint(1, 10) for i in range(20)]
print(data, data.__len__())
pool = threadpool.ThreadPool(5)
requests = threadpool.makeRequests(worker_get, data, print_result)
[pool.putRequest(req) for req in requests]
pool.wait()
