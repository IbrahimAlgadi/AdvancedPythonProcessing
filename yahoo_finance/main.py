import time
# from multiprocessing import Queue
# from workers.yahoo_finance_worker import YahooFinancePriceScheduler
from workers.wiki_worker import WikiWorker
# from workers.postgres_worker import PostgresMasterScheduler
from yaml_reader import YamlPipelineExecutor

"""
Adding Queue 
> Queue Consumers
> Queue Producers
"""


def main():
    yaml_pipeline_executor = YamlPipelineExecutor(pipeline_location='pipelines/wiki_yahoo_scrapper_pipeline.yaml')

    # symbol_queue = Queue()
    # postgres_queue = Queue()

    calc_start_time = time.time()

    wiki_worker = WikiWorker()
    # yahoo_finance_price_scheduler_threads = []
    # TODO: Now we have 5 workers each one is
    #   waiting for the queue to have a value and start
    #   immediatly once it get the value from the queue
    # num_yahoo_finance_workers = 4
    # for i in range(num_yahoo_finance_workers):
    #     yahoo_finance_price_scheduler = YahooFinancePriceScheduler(
    #         input_queue=symbol_queue,
    #         output_queue=postgres_queue
    #     )
    #     yahoo_finance_price_scheduler_threads.append(yahoo_finance_price_scheduler)

    # TODO: Adding Postgres Scheduler Queue Subscribe and Publish
    # postgres_scheduler_threads = []
    # num_postgres_workers = 2
    # for i in range(num_postgres_workers):
    #     postgres_scheduler = PostgresMasterScheduler(
    #         input_queue=postgres_queue
    #     )
    #     postgres_scheduler_threads.append(postgres_scheduler)

    symbol_counter = 0
    for symbol in wiki_worker.get_sp_500_companies():
        yaml_pipeline_executor._queues['SymbolQueue'].put(symbol)
        # symbol_queue.put(symbol)
        print(symbol)
        symbol_counter += 1
        if symbol_counter >= 4:
            print("[*] Break")
            break

    # TODO: To Break Every Thread We Need to Put Many DONE so all
    #       other threads stops
    for i in range(20):
        yaml_pipeline_executor._queues['SymbolQueue'].put('DONE')

    # TODO: Block the program to wait for all the threads to finish
    yaml_pipeline_executor._join_workers()

    # # TODO: To Break Every Thread We Need to Put Many DONE so all
    # #       other threads stops
    # for i in range(len(postgres_scheduler_threads)):
    #     postgres_queue.put('DONE')
    #
    # # # TODO: Block the program to wait for all the threads to finish
    # # for i in range(len(postgres_scheduler_threads)):
    # #     postgres_scheduler_threads[i].join()

    print("[*] Extracting Time Took: ", round(time.time() - calc_start_time, 1))


if __name__ == '__main__':
    main()
