import requests
from bs4 import BeautifulSoup


class WikiWorker():
    def __init__(self):
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

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
        response = requests.get(self._url)

        if response.status_code != 200:
            print("[*] Coudn't get entries ...")
            return []

        yield from self._extract_company_symbols(response.text)


if __name__ == '__main__':
    wiki_worker = WikiWorker()
    symbols = []

    for symbol in wiki_worker.get_sp_500_companies():
        # print(symbol)
        symbols.append(symbol)

    print(len(symbols))
