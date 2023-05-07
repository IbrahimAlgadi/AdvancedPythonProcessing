from multiprocessing import Pool
from multiprocessing import cpu_count
from multiprocessing import freeze_support
from functools import partial
import time


def square(y, to_add, x):
    return x**y+to_add


num_processes = 4
comparison_list = [1, 2, 3]
power = 3
to_add = 2
num_cpu_to_use = max(1, cpu_count() - 1)
# print(num_cpu_to_use)

partial_function = partial(square, power, to_add)

if __name__ == '__main__':
    freeze_support()

    start_time = time.time()

    with Pool(num_cpu_to_use) as ap_pool:
        result = ap_pool.map(partial_function, comparison_list)

    print(result)

    print("[*] Everything Took: ", time.time() - start_time, 'seconds')
