import requests
import time

class Timer:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.elapsed = self.end - self.start
        print('%s took: %0.3f sec' % (self.name, self.elapsed))
        return False


if __name__ == '__main__':
    with Timer('fetching github homepage'):
        r = requests.get('https://github.com')