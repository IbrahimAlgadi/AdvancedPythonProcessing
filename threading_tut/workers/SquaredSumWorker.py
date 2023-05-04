import threading


class SquaredSumWorker(threading.Thread):

    def __init__(self, n, *args, **kwargs):
        self._n = n
        self.daemon = True
        super(SquaredSumWorker, self).__init__(*args, **kwargs)
        # start the thread
        self.start()

    def _calculate_sum_squares(self):
        """
        To Speedup This Section We Need Multiprocessing For Computation
        :return:
        """
        sum_squares = 0
        for i in range(self._n):
            sum_squares += i ** 2

        print(sum_squares)

    def run(self) -> None:
        self._calculate_sum_squares()
