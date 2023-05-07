from threading import Thread
import time


def check_value_in_list(x):
    for i in range(10 ** 8):
        i in x


num_threads = 4
comparison_list = [1, 2, 3]

start_time = time.time()

threads: [Thread] = []
for i in range(num_threads):
    t = Thread(target=check_value_in_list, args=(comparison_list,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("[*] Everything Took: ", time.time() - start_time, 'seconds')
