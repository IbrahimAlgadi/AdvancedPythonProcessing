import time
from multiprocessing import Queue
from workers.yahoo_finance_worker import YahooFinancePriceScheduler
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
    yahoo_finance_price_scheduler_threads = []
    # TODO: Now we have 5 workers each one is
    #   waiting for the queue to have a value and start
    #   immediatly once it get the value from the queue
    num_yahoo_finance_workers = 5
    for i in range(num_yahoo_finance_workers):
        yahoo_finance_price_scheduler = YahooFinancePriceScheduler(
            input_queue=symbol_queue
        )
        yahoo_finance_price_scheduler_threads.append(yahoo_finance_price_scheduler)

    for symbol in wiki_worker.get_sp_500_companies():
        symbol_queue.put(symbol)

    # TODO: To Break Every Thread We Need to Put Many DONE so all
    #       other threads stops
    for i in range(len(yahoo_finance_price_scheduler_threads)):
        symbol_queue.put('DONE')

    # TODO: Block the program to wait for all the threads to finish
    for i in range(len(yahoo_finance_price_scheduler_threads)):
        yahoo_finance_price_scheduler_threads[i].join()

    print("[*] Extracting Time Took: ", round(time.time() - calc_start_time, 1))


if __name__ == '__main__':
    main()
