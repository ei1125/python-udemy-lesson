# logging formatter

"""
https://docs.python.org/ja/3/howto/logging.html
"""

import logging

# formatter = '%(levelname)s:%(message)s'
formatter = '%(asctime)s:%(message)s'

logging.basicConfig(level=logging.INFO, format=formatter)

logging.info('info %s %s','test', 'test2')