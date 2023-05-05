import importlib
import threading

import yaml
from multiprocessing import Queue


class YamlPipelineExecutor(threading.Thread):

    def __init__(self, pipeline_location, **kwargs):
        self._pipeline_location = pipeline_location
        self._queues = {}
        self._workers = {}

        super(YamlPipelineExecutor, self).__init__(**kwargs)
        self.start()

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
        self._join_workers()

    def run(self):
        self.process_pipeline()

        while True:
            pass


if __name__ == '__main__':
    pass
