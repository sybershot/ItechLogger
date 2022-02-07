import datetime
import functools

LOGS_PATH = '../logs/latest.log'


def log_method_call(fun, logger):  # This is decorator.
    @functools.wraps(fun)  # fun == function
    def wrapper(*args, **kwargs):
        try:
            result = fun(*args, **kwargs)
            if result is None:
                logger.warning(f"Function {fun.__name__!r} returned None")
            else:
                logger.info(f"Function {fun.__name__!r} Returned {result!r}")
            return result
        except Exception as e:
            logger.error(f"Caught exception in {fun.__name__!r}", e)

    return wrapper


class CallLogger(type):  # Singleton CallLogger class. It intercepts calls!
    _instances = {}

    def __new__(mcs, name, bases, attrs, logger):
        for key in attrs.keys():
            if callable(attrs[key]):
                fun = attrs[key]
                attrs[key] = log_method_call(fun, logger)
        return super().__new__(mcs, name, bases, attrs)


class Logger:  # Singleton Logger
    __instance = None

    def __new__(cls):
        if not Logger.__instance:
            Logger.__instance = super(Logger, cls).__new__(cls)
        return Logger.__instance

    def __init__(self):
        self.logger = open(LOGS_PATH, "w", encoding='utf-8')

    @staticmethod
    def _get_time():
        return datetime.datetime.now().strftime('%x %X')

    @staticmethod
    def log_to_console(message):
        print(message)

    def write_to_file(self, message):
        self.log_to_console(message)
        self.logger.write(message + '\n')

    def info(self, message):
        self.write_to_file(f'{self._get_time()} [INFO]: {message}')

    def warning(self, message):
        self.write_to_file(f'{self._get_time()} [WARN]: {message}')

    def error(self, message, exception: Exception):
        self.write_to_file(f'{self._get_time()} [ERROR]: {message}: {exception!r}')
