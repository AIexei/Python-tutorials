import time
import logging
from functools import wraps


def logit(level):
    def decorator(func):
        log = logging.getLogger(func.__name__)
        logging.basicConfig(level=level)

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.info('begin')
            res = func(*args, **kwargs)
            log.info('end')
            return res

        return wrapper
    return decorator


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t_start
        print('time -> [%0.5fs]' % (elapsed))
        return result

    return wrapper

@logit(logging.DEBUG)
@timeit
def add(num):
    alist = []

    for i in range(num):
        alist.append(i)


if __name__ == '__main__':
    add(1000)
