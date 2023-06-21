"""decorator for modules.accelerate() method"""
import logging
from functools import wraps


def logged(arg_exception, arg_mode):
    """out Transport accelerate exception"""

    def logger(func):
        @wraps(func)
        def inner(*args, **kwargs):
            res = None
            try:
                res = func(*args, **kwargs)
            except arg_exception:
                if arg_mode == "file":
                    logging.basicConfig(filename="output.log",
                                        format=f"%(asctime)s:%(levelname)s:"
                                               f"{func.__name__}():%(message)s")
                    logging.error(arg_exception())
                if arg_mode == "console":
                    logging.basicConfig(format=f"%(asctime)s:%(levelname)s:"
                                               f"{func.__name__}():%(message)s")
                    logging.error(arg_exception())
            return res

        return inner

    return logger
