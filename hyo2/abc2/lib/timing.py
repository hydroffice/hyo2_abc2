import logging
import time
import functools

logger = logging.getLogger(__name__)

def time_execution(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start  # seconds
            if elapsed > 600:
                logger.info(f"{func.__qualname__} executed in {elapsed/60:.3f} minutes")
            else:
                logger.info(f"{func.__qualname__} executed in {elapsed:.3f} seconds")

    return wrapper
