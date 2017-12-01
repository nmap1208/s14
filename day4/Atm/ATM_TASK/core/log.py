#Auther nmap
import logging
from conf import setting
from core import db_handle

def log(logging_type):
    logger=logging.getLogger(logging_type)
    logger.setLevel(setting.LOGIN_LEVEL)

    ch=logging.StreamHandler()
    ch.setLevel(setting.LOGIN_LEVEL)

    log_file='%s/logs/%s'%(setting.BASE_DIR,setting.LOGIN_TYPE[logging_type])
    fh=logging.FileHandler(log_file)
    fh.setLevel(setting.LOGIN_LEVEL)

    formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger
