import logging

def setup_logger():
    """
    Set up the logger for logging events during the analysis process.
    
    Returns:
        logger: A configured logger.
    """
    logger = logging.getLogger('ChainMagLogger')
    handler = logging.FileHandler('logs/analysis_log.txt')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

# Example of logging in use
logger = setup_logger()
logger.info("Analysis started.")
