import time
from multiprocessing import Queue
from workers.yahoo_finance_worker import YahooFinanceWorker
from workers.wiki_worker import WikiWorker

"""
Adding Queue 
> Queue Consumers
> Queue Producers
"""


def main():
    symbol_queue = Queue()

    calc_start_time = time.time()

    wiki_worker = WikiWorker()
    current_threads = []
    for symbol in wiki_worker.get_sp_500_companies():
        # insert symbol to queue
        # queues are thread safe
        symbol_queue.put(symbol)

        # yahoo_finance_worker = YahooFinanceWorker(symbol=symbol)
        # # yahoo_finance_worker.join()
        # current_threads.append(yahoo_finance_worker)
        # # print(current_threads)
        # if len(current_threads) == 5:
        #     # TODO: Block the program to wait for all the threads to finish
        #     for i in range(len(current_threads)):
        #         current_threads[i].join()
        #     current_threads = []

    # TODO: Block the program to wait for all the threads to finish
    # for i in range(len(current_threads)):
    #     current_threads[i].join()

    print(symbol_queue)
    print(symbol_queue.get())

    print("[*] Extracting Time Took: ", round(time.time() - calc_start_time, 1))


if __name__ == '__main__':
    main()
