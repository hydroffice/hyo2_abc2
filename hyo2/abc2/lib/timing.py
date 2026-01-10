import logging
import time
import functools

logger = logging.getLogger(__name__)

def time_execution(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        logger.info(f"{func.__name__} executed in {elapsed:.6f} seconds")
        return result

    return wrapper
