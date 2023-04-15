import logging

# logging.basicConfig(level=logging.ERROR)
logging.basicConfig(filename='my_logs.log',
                    encoding='utf-8')


logging.debug('DEBUG')
logging.info('INFO')
logging.warning('WARNING')
logging.error('ERROR')
logging.critical('CRITICAL')
