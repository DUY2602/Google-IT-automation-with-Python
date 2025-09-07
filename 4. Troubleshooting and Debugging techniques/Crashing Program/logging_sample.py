import logging

logging.basicConfig (
    filename='sample.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.warning('This is a warning message')
logging.error('This is an error message')
logging.debug('This is a debug message')
logging.info('This message will be written to app.log')
logging.error('This is an error with a custom format')