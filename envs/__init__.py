from loguru import logger
import os

try:
    os.mkdir('logs')
except:
    pass


def get_logger(name: str) -> logger:
    logger.add(f'./logs/{name}_error.log', format="{time} {level} {name}:{function}:{line} {message}",
               level="ERROR")
    logger.add(f'./logs/{name}_warning.log', format="{time} {level} {name}:{function}:{line} {message}",
               level="WARNING")
    logger.add(f'./logs/{name}_debug.log', format="{time} {level} {name}:{function}:{line} {message}",
               level="DEBUG")
    logger.add(f'./logs/{name}_info.log', format="{time} {level} {name}:{function}:{line} {message}",
               level="INFO")
    return logger

