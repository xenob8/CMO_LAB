import logging

logging.basicConfig(filename="log.log", level=logging.DEBUG, filemode='w')
a = 5
logging.info(msg=f'msg {a}')

