# import threading as tr
# # from time import sleep, time
# import time

# def foo(num):
#     print(tr.current_thread())
#     sleep(2)
#     print(num)


# start = time()
# print(tr.current_thread())
# thr1 = tr.Thread(target=foo, args=(1, ))
# thr2 = tr.Thread(target=foo, args=(2, ))

# thr1.start()
# thr2.start()

# thr1.join()
# thr2.join()

# print(f'Done in: {time()-start}')
#-----------------------------------
# def foo(num):
#     print(tr.current_thread())
#     sleep(num)


# start = time()
# threads = []
# for i in range(10):
#     thr1 = tr.Thread(target=foo, args=(1, ))
#     thr1.start()
#     threads.append(thr1)

# while threads:
#     print(threads, len(threads))
#     sleep(0.5)
#     for index, th in enumerate(threads):
#         if not th.is_alive():
#             threads.pop(index)


# print('Done')

# #---------------------------------
# import os
# import requests
# import time
# import threading as th

# def save_image():
#     url = 'https://loremflickr.com/320/240/dog'
#     response = requests.get(url)
#     name = response.url.split('/')[-1]
#     path = os.path.join(os.getcwd(), 'images', name)

#     with open(path, 'wb') as file:
#         file.write(response.content)

# start = time.time()
# threads = []
# for _ in range(100):
#     t = th.Thread(target=save_image)
#     t.start()
#     threads.append(t)

# for th in threads:
#     th.join()
# print(time.time() - start)

# #---------------------------------
# Многопоточность в многопроцессинг
# import os
# import requests
# from multiprocessing.pool import ThreadPool

# def save_image(*args):
#     url = 'https://loremflickr.com/320/240/dog'
#     response = requests.get(url)
#     name = response.url.split('/')[-1]
#     path = os.path.join(os.getcwd(), 'images', name)

#     with open(path, 'wb') as file:
#         file.write(response.content)


# start = time.time()
# with ThreadPool(25) as pool:
#     pool.map(save_image, range(100))
# print(time.time() - start)

# #===============================
# import time
# import threading as tr


# count = 500_000_000

# def countdown(n):
#     while n > 0:
#         n-=1

# start = time.time()
# countdown(count)
# print(time.time() - start)

# #===============================
# import time
# import threading as tr


# count = 500_000_000

# def countdown(n):
#     while n > 0:
#         n-=1

# start = time.time()
# t1 = tr.Thread(target=countdown, args=(count//2, ))
# t2 = tr.Thread(target=countdown, args=(count//2, ))

# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print(time.time() - start)

# #===============================
# import time
# import threading as tr
# import multiprocessing as mpr

# cpu_count = mpr.cpu_count()*2
# print(cpu_count)

# count = 500_000_000

# def countdown(n):
#     while n > 0:
#         n-=1

# start = time.time()
# p1 = mpr.Process(target=countdown, args=(count//2, ))
# p2 = mpr.Process(target=countdown, args=(count//2, ))

# p1.start()
# p2.start()

# p1.join()
# p2.join()
# print(time.time() - start)

#===============================
import time
import threading as tr
import multiprocessing as mpr

cpu_count = mpr.cpu_count()*2
print(cpu_count)

count = 500_000_000

def countdown(n):
    while n > 0:
        n-=1

start = time.time()
processes = []
for i in range(cpu_count):
    p1 = mpr.Process(target=countdown, args=(count//cpu_count, ))
    p1.start()
    processes.append(p1)

for p in processes:
    p.join()


print(time.time() - start)