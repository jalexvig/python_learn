import logging

logger = logging.getLogger(__name__)

class Filter(logging.Filter):

    def filter(self, record):
        print(record.__dict__)
        return True

if __name__ == '__main__':

    logger.addFilter(Filter())
    logger.warning('BOOGLY')
