import os
import time

from dotenv import load_dotenv

from yaml_reader import YamlPipelineExecutor

"""
Adding Queue 
> Queue Consumers
> Queue Producers
"""


def main():
    # TODO: load environment .env file
    load_dotenv(dotenv_path='.env_local')

    calc_start_time = time.time()
    pipeline_location = os.environ.get('PIPELINE_LOCATION')

    if pipeline_location is None:
        print("[*] Pipeline location is not defined ...")
        exit(1)

    yaml_pipeline_executor = YamlPipelineExecutor(pipeline_location=pipeline_location)
    yaml_pipeline_executor.start()

    print("[*] Extracting Time Took: ", round(time.time() - calc_start_time, 1))


if __name__ == '__main__':
    main()
