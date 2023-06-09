from multiprocessing import Process, freeze_support
import time


def check_value_in_list(x):
    for i in range(10 ** 8):
        i in x


num_processes = 4
comparison_list = [1, 2, 3]

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
        t = Process(target=check_value_in_list, args=(comparison_list,))
        processes.append(t)

    for t in processes:
        t.start()

    for t in processes:
        t.join()

    print("[*] Everything Took: ", time.time() - start_time, 'seconds')
