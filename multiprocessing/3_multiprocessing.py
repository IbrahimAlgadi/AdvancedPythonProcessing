from multiprocessing import Process
from multiprocessing import freeze_support
from multiprocessing import Queue
import time


def check_value_in_list(x, i, num_processes, queue):
    max_number_to_check_to = 10 ** 8

    lower = int(i * max_number_to_check_to / num_processes)
    upper = int((i + 1) * max_number_to_check_to / num_processes)

    num_hits = 0

    for i in range(lower, upper):
        if i in x:
            num_hits += 1

    queue.put((lower, upper, num_hits))


num_processes = 4
queue = Queue()
comparison_list = [1, 2, 3, 25000000]

if __name__ == '__main__':
    # We are using more than one Core in the program
    """
    
    Each and every process executes in a new core
    with its own GIL and python interpreter
    
    -> Network IO (threading)
    -> CPU utilization (Multiprocessing)
    
    """
    freeze_support()

    start_time = time.time()

    processes = []
    for i in range(num_processes):
        t = Process(target=check_value_in_list, args=(comparison_list, i, num_processes, queue))
        processes.append(t)

    for t in processes:
        t.start()

    for t in processes:
        t.join()

    queue.put('DONE')

    while True:
        v = queue.get()
        if v == 'DONE':
            break

        lower, upper, num_hits = v
        print("Between", lower, "and", upper, "we have", num_hits, "values in this list")

    print("[*] Everything Took: ", time.time() - start_time, 'seconds')
