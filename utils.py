from logging import Logger, getLogger, StreamHandler, DEBUG, Formatter


def setup_logger(name: str) -> Logger:
    logger = getLogger(name)
    logger.setLevel(DEBUG)
    console_handler = StreamHandler()
    console_handler.setLevel(DEBUG)
    formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger