import threading
import requests
from lxml import html
# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


class YahooFinanceWorker(threading.Thread):

    def __init__(self, symbol, **kwargs):
        self._symbol = symbol
        self._url = f'https://finance.yahoo.com/quote/{self._symbol}'

        super(YahooFinanceWorker, self).__init__(**kwargs)

        self.start()

    def run(self) -> None:
        # print()
        # return
        # TODO: So we dont spam we need to sleep
        time.sleep(30 * random.random())
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
            print(self._symbol, "\t\tPRICE: ", finance_price_value)
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
