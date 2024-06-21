"""
Authors: guanchenglichina@qq.com (Guancheng Li)

The format for logging.
"""

import logging
import os


def set_logger(logging_path: str, filename: str):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logging_formatter = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)s] %(message)s'
    log_path = os.path.join(logging_path, f'log/{filename}.log')
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    handler = logging.FileHandler(log_path, 'w')
    formatter = logging.Formatter(logging_formatter)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    str_handler = logging.StreamHandler()
    str_handler.setLevel(logging.ERROR)
    str_formatter = logging.Formatter(logging_formatter)
    str_handler.setFormatter(str_formatter)
    logger.addHandler(str_handler)
