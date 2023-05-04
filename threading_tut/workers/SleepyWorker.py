import threading
import time


class SleepyWorker(threading.Thread):

    def __init__(self, seconds, *args, **kwargs):
        self._seconds = seconds
        self.daemon = True
        super(SleepyWorker, self).__init__(*args, **kwargs)
        self.start()

    def _sleep_a_little(self):
        time.sleep(self._seconds)

    def run(self) -> None:
        self._sleep_a_little()
