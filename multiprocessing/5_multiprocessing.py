from multiprocessing import Pool
from multiprocessing import cpu_count
from multiprocessing import freeze_support
from functools import partial
import time


def square(x, y):
    return x ** y


num_processes = 4
comparison_list = [1, 2, 3]
power_list = [4, 5, 6]
num_cpu_to_use = max(1, cpu_count() - 1)
print("CPU USED: ", num_cpu_to_use)

prepared_list = list(zip(comparison_list, power_list))
print(prepared_list)

if __name__ == '__main__':
    freeze_support()


    start_time = time.time()

    with Pool(num_cpu_to_use) as ap_pool:
        result = ap_pool.starmap(square, prepared_list)

    print(result)

    print("[*] Everything Took: ", time.time() - start_time, 'seconds')
