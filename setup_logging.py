import logging
import sys


def setup_logging():
    logger = logging.getLogger("benchmarking")
    logger.setLevel(logging.INFO)

    # Create a StreamHandler to output logs to stdout
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)

    # Define the log format
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(log_format)

    # Add the StreamHandler to the logger
    logger.addHandler(stream_handler)

    return logger