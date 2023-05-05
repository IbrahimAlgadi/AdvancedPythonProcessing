import time
from yaml_reader import YamlPipelineExecutor

"""
Adding Queue 
> Queue Consumers
> Queue Producers
"""


def main():

    calc_start_time = time.time()

    yaml_pipeline_executor = YamlPipelineExecutor(pipeline_location='pipelines/wiki_yahoo_scrapper_pipeline.yaml')
    yaml_pipeline_executor.start()

    print("[*] Extracting Time Took: ", round(time.time() - calc_start_time, 1))


if __name__ == '__main__':
    main()
