import time
from workers.SleepyWorker import SleepyWorker
from workers.SquaredSumWorker import SquaredSumWorker


def main():
    calc_start_time = time.time()

    current_threads = []
    for i in range(5):
        maximum_value = ((i + 1) * 1000_000)
        squared_sum_worker = SquaredSumWorker(n=maximum_value, daemon=True)
        current_threads.append(squared_sum_worker)

    # TODO: Block the program to wait for all the threads to finish
    for i in range(len(current_threads)):
        current_threads[i].join()

    print("[*] Calculate sum of squares took: ", round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()

    current_threads = []
    for i in range(1, 6):
        sleepy_worker = SleepyWorker(seconds=i, daemon=True)
        current_threads.append(sleepy_worker)

    # TODO: Block the program to wait for all the threads to finish
    for i in range(len(current_threads)):
        current_threads[i].join()

    print("[*] Calculate sum of squares took: ", round(time.time() - sleep_start_time, 1))


if __name__ == '__main__':
    main()
