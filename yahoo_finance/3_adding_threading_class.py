import time
from workers.yahoo_finance_worker import YahooFinanceWorker
from workers.wiki_worker import WikiWorker


def main():
    calc_start_time = time.time()

    wiki_worker = WikiWorker()
    current_threads = []
    for symbol in wiki_worker.get_sp_500_companies():
        yahoo_finance_worker = YahooFinanceWorker(symbol=symbol)
        # yahoo_finance_worker.join()
        current_threads.append(yahoo_finance_worker)
        # print(current_threads)
        if len(current_threads) == 5:
            # TODO: Block the program to wait for all the threads to finish
            for i in range(len(current_threads)):
                current_threads[i].join()
            current_threads = []

    # TODO: Block the program to wait for all the threads to finish
    # for i in range(len(current_threads)):
    #     current_threads[i].join()

    print("[*] Extracting Time Took: ", round(time.time() - calc_start_time, 1))


if __name__ == '__main__':
    main()
