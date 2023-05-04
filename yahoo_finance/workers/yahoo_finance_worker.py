import threading
# import requests
# from lxml import html
# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from queue import Empty
import time, datetime
import random


class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self, input_queue, output_queue, **kwargs):
        super(YahooFinancePriceScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue
        self._output_queue = output_queue
        self.start()

    def run(self) -> None:
        while True:
            print("[*] Started Yahoo Thread ...")
            try:
                val = self._input_queue.get(timeout=10)
            except Empty:
                print("[*] Yahoo Finance Timeout ...")
                break
            print("YAHOOO VAL: ", val)
            if val == 'DONE':
                # if self._output_queue is not None:
                #     self._output_queue.put('DONE')
                break

            yahoo_finance_worker = YahooFinanceWorker(symbol=val)
            price = 100  # yahoo_finance_worker.get_price()
            print(val, "\t\tPRICE: ", price)
            if self._output_queue is not None:
                output_value = [val, price, datetime.datetime.utcnow()]
                self._output_queue.put(output_value)
            # TODO: So we dont spam we need to sleep
            time.sleep(5 * random.random())


class YahooFinanceWorker:

    def __init__(self, symbol, **kwargs):
        self._symbol = symbol
        self._url = f'https://finance.yahoo.com/quote/{self._symbol}'
        super(YahooFinanceWorker, self).__init__(**kwargs)

    def get_price(self):
        ########################################
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument('--log-level=3')
        # Provide the path of chromedriver present on your system.
        driver = webdriver.Chrome(
            executable_path=str(__file__).replace('yahoo_finance_worker.py', 'chromedriver.exe'),
            chrome_options=options
        )
        driver.get(self._url)
        try:
            finance_price_value = driver.find_elements(
                by=By.XPATH,
                value='//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]'
            )[0].text
            # if the number is 1,234 => replace , comma with ''
            return float(finance_price_value.replace(',', ''))
        except Exception as e:
            print("Error: ", e)
            return


if __name__ == '__main__':
    # response = requests.get('https://finance.yahoo.com/quote/AAPL')
    # print(response.text)
    # lxml_parse = html.fromstring(response.text)
    # print(lxml_parse)
    # page_content = lxml_parse.xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/div/div[3]/div[1]/div/fin-streamer[1]/span')
    # print(page_content)

    pass
