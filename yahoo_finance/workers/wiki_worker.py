import threading
import time

import requests
from bs4 import BeautifulSoup


class WikiWorkerMasterScheduler(threading.Thread):
    def __init__(self, output_queue, **kwargs):
        if 'input_queue' in kwargs: kwargs.pop('input_queue')
        self._input_values = kwargs.pop('input_values')
        print("Output Queue: ", output_queue)
        self._output_queues = [output_queue] if type(output_queue) != list else output_queue
        super(WikiWorkerMasterScheduler, self).__init__(**kwargs)
        self.start()

    def run(self) -> None:
        for input_value in self._input_values:
            wiki_worker = WikiWorker(input_value)

            symbol_counter = 0
            for symbol in wiki_worker.get_sp_500_companies():
                for output_queue in self._output_queues:
                    output_queue.put(symbol)
                symbol_counter += 1
                if symbol_counter >= 4:
                    print("[*] Break")
                    break
        # print(self._output_queues)
        # for output_queue in self._output_queues:
        #     for i in range(20):
        #         output_queue.put('DONE')


class WikiWorker:
    def __init__(self, url):
        self._url = url

    @staticmethod
    def _extract_company_symbols(page_html):
        soup = BeautifulSoup(page_html, features="html.parser")
        table = soup.find(id='constituents')
        table_rows = table.find_all('tr')

        for table_row in table_rows[1:]:
            symbol = table_row.find('td').text.strip('\n')
            # print("SYMBOL: ", symbol)
            yield symbol

    def get_sp_500_companies(self):
        time.sleep(3)
        for i in range(5):
            yield 'AML'

        # response = requests.get(self._url)
        #
        # if response.status_code != 200:
        #     print("[*] Coudn't get entries ...")
        #     return []
        #
        # yield from self._extract_company_symbols(response.text)


if __name__ == '__main__':
    wiki_worker = WikiWorker()
    symbols = []

    for symbol in wiki_worker.get_sp_500_companies():
        # print(symbol)
        symbols.append(symbol)

    print(len(symbols))
