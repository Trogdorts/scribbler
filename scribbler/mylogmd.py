import sys
import logging

def startlogging():
    logger = logging.getLogger('')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('my_log_info.log')
    sh = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s',
                                  datefmt='%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    logger.handlers.clear()
    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger

