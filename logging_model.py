import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d, %Y, %H, %S',
                    filename='test.log',
                    # filemode='a'
                    )

logging.debug('debug message')
logging.info('info message')
logging.warn('warning message')
logging.error('error message')
logging.critical('critical message')




