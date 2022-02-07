from utils.ilogger.logger import CallLogger, Logger

logger = Logger()


class TestSteps(metaclass=CallLogger, logger=logger):
    def raise_exception(self):
        raise Exception("This is an Exception!")

    def return_none(self):
        return None

    def return_hello(self, name):
        return f'Hello, {name}!'

    def test_defaults(self, name):
        self.raise_exception()
        self.return_none()
        self.return_hello(name)
