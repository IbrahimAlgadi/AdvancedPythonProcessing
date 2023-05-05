import importlib
import threading
import time

import yaml
from multiprocessing import Queue


class YamlPipelineExecutor(threading.Thread):

    def __init__(self, pipeline_location, **kwargs):
        self._pipeline_location = pipeline_location
        self._queues = {}
        self._workers = {}

        # what queues are writing
        self._queue_consumers = {}
        # what workers are reading
        self._downstream_queue = {}

        super(YamlPipelineExecutor, self).__init__(**kwargs)
        # self.start()

    def _load_pipeline(self):
        print("[*] Loading Pipeline ...")
        with open(self._pipeline_location, 'r') as inFile:
            self._yaml_data = yaml.safe_load(inFile)
        print("[*] Done ...")

    def _initialize_queues(self):
        print("[*] Initialize Queues ...")
        for queue in self._yaml_data['queues']:
            queue_name = queue['name']
            self._queues[queue_name] = Queue()

        print("[*] Done ...")

    def _initialize_workers(self):
        print("[*] Initialize Worker Classes ...")
        for worker in self._yaml_data['workers']:
            _WorkerClass = getattr(importlib.import_module(worker['location']), worker['class'])
            # print("[*] Worker Class: ", _WorkerClass.__name__)
            input_queue = worker.get('input_queue')
            output_queues = worker.get('output_queues')
            worker_name = worker['name']
            num_instances = worker.get('instances', 1)

            # what queue worker is writing to
            self._downstream_queue[worker_name] = output_queues
            if input_queue is not None:
                # how many workers are consuming
                # the output queue as input for them
                self._queue_consumers[input_queue] = num_instances

            init_params = {
                'input_queue': self._queues[input_queue] if input_queue is not None else None,
                'output_queue': [self._queues[output_queue] for output_queue in
                                 output_queues] if output_queues is not None else None,
            }
            # Add input_value params for wiki worker if its set
            input_values = worker.get('input_values')
            if input_values is not None:
                init_params['input_values'] = input_values

            # TODO: Create Workers List
            self._workers[worker_name] = []
            for i in range(num_instances):
                self._workers[worker_name].append(_WorkerClass(**init_params))
                # print("[*] Workers: ", self._workers)
        print("[*] Done ...")

    def _join_workers(self):
        for worker_name in self._workers:
            for worker_thread in self._workers[worker_name]:
                worker_thread.join()

    def process_pipeline(self):
        # TODO: First Load the Pipeline
        self._load_pipeline()
        # TODO: Then Initialize The Queues
        self._initialize_queues()
        # TODO: Then Initialize The Workers
        self._initialize_workers()
        # TODO: Then Join The Workers
        # self._join_workers()

    def run(self):
        self.process_pipeline()

        while True:
            total_workers_alive = 0
            worker_stats = []
            # Monitor the queue if it is still running
            # when the wiki worker break from the run loop
            # then send DONE in the output queue targeting
            # the next workers

            workers = self._workers.copy()

            for worker_name in workers:
                total_worker_threads_alive = 0
                for worker_thread in self._workers[worker_name]:
                    if worker_thread.is_alive():
                        total_worker_threads_alive += 1

                total_workers_alive += total_worker_threads_alive

                if total_worker_threads_alive == 0:
                    # for each output queue how many threads are reading
                    # from it
                    if self._downstream_queue[worker_name] is not None:
                        for output_queue in self._downstream_queue[worker_name]:
                            num_of_consumers = self._queue_consumers[output_queue]
                            # send done signal for all the consumers listening to
                            # this output queue once it is done
                            for i in range(num_of_consumers):
                                self._queues[output_queue].put('DONE')
                    # delete that specific worker if it is not
                    # alive to stop tracking it

                    del self._workers[worker_name]

                worker_stats.append([worker_name, total_worker_threads_alive])

            print(f"[*] TOTAL THREADS ALIVE {worker_stats}")

            if total_workers_alive == 0:
                break

            queue_stats = []
            for queue in self._queues:
                queue_stats.append([queue, self._queues[queue].qsize()])
            print("Queue Size: ", queue_stats)

            time.sleep(1)


if __name__ == '__main__':
    pass
