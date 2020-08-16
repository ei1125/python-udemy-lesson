import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# logtest.logのファイルに書き込まれる
h = logging.FileHandler('logtest.log')
logger.addHandler(h)

def do_something():
    logging.info('from logtest info')
    logger.info('from logtest')
    logger.debug('from logtest debug')