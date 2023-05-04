import os
import threading
from sqlalchemy import create_engine
from sqlalchemy.sql import text


class PostgresMasterScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        super(PostgresMasterScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()

    def run(self) -> None:
        while True:
            val = self._input_queue.get()
            if val == 'DONE':
                break
            symbol, price, extracted_time = val
            postgres_worker = PostgresWorker(
                symbol=symbol,
                price=price,
                extracted_time=extracted_time,
            )
            postgres_worker.insert_into_db()


class PostgresWorker:

    def __init__(self, symbol, price, extracted_time, **kwargs):
        self._symbol = symbol
        self._price = price
        self._extracted_time = extracted_time

        # POSTGRES CONNECTION
        self._PG_USER = os.environ.get("PG_USER", 'postgres')
        self._PG_PW = os.environ.get("PG_PW", 'postgres')
        self._PG_HOST = os.environ.get("PG_HOST", 'localhost')
        self._PG_DB = os.environ.get("PG_DB", 'postgres')
        # POSTGRES CONNECTION
        self._engine = create_engine(f"postgresql://{self._PG_USER}:{self._PG_PW}@{self._PG_HOST}/{self._PG_DB}")

    def _create_insert_query(self):
        SQL = f"""
INSERT INTO prices (symbol, price, extracted_time) VALUES (:symbol, :price, :extracted_time)
        """
        return SQL

    def insert_into_db(self):
        insert_query = self._create_insert_query()
        with self._engine.connect() as conn:
            conn.execute(
                text(insert_query),
                {
                    'symbol': self._symbol,
                    'price': self._price,
                    'extracted_time': self._extracted_time,
                }
            )


if __name__ == '__main__':
    # response = requests.get('https://finance.yahoo.com/quote/AAPL')
    # print(response.text)
    # lxml_parse = html.fromstring(response.text)
    # print(lxml_parse)
    # page_content = lxml_parse.xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/div/div[3]/div[1]/div/fin-streamer[1]/span')
    # print(page_content)

    pass
