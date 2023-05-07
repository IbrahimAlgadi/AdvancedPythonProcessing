from multiprocessing import Pool
from multiprocessing import cpu_count
from multiprocessing import freeze_support
from functools import partial
import time


def check_num_of_values_in_range(comp_list, lower, upper):
    num_hits = 0
    for i in range(lower, upper):
        if i in comp_list:
            num_hits += 1
    return num_hits


num_processes = 4
comparison_list = [1, 2, 3]
lower_and_upper_bounds = [
    (0, 25 * 10 ** 6),
    (25 * 10 ** 6, 50 * 10 ** 6),
    (50 * 10 ** 6, 75 * 10 ** 6),
    (75 * 10 ** 6, 10 ** 8),
]
num_cpu_to_use = max(1, cpu_count() - 1)
# print("CPU USED: ", num_cpu_to_use)

prepared_list = []
for i in range(len(lower_and_upper_bounds)):
    prepared_list.append((comparison_list, *lower_and_upper_bounds[i]))
# print(prepared_list)

if __name__ == '__main__':
    freeze_support()

    start_time = time.time()

    with Pool(num_cpu_to_use) as ap_pool:
        result = ap_pool.starmap(check_num_of_values_in_range, prepared_list)

    print(result)

    print("[*] Everything Took: ", time.time() - start_time, 'seconds')
