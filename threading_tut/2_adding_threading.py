import time
import threading


def calculate_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i ** 2

    print(sum_squares)


def sleep_a_little(seconds):
    time.sleep(seconds)


def main():
    calc_start_time = time.time()

    # replace each loop with a thread
    current_threads = []
    for i in range(5):
        maximum_value = ((i + 1) * 1000_000)
        t = threading.Thread(
            target=calculate_sum_squares,
            args=(maximum_value,)
        )
        # if you didnt call t.start it will not do anything
        t.start()
        current_threads.append(t)
        # calculate_sum_squares((i + 1) * 1000_000)

    # TODO: Block the program to wait for all the threads to finish
    for i in range(len(current_threads)):
        current_threads[i].join()
    print("[*] Calculate sum of squares took: ", round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()

    # create thread for each sleep function
    current_threads = []
    for i in range(1, 6):
        t = threading.Thread(
            target=sleep_a_little,
            args=(i,)
        )
        # if you didnt call t.start it will not do anything
        t.start()
        current_threads.append(t)
        # sleep_a_little(i)

    # TODO: Block the program to wait for all the threads to finish
    for i in range(len(current_threads)):
        current_threads[i].join()

    print("[*] Calculate sum of squares took: ", round(time.time() - sleep_start_time, 1))


if __name__ == '__main__':
    main()
