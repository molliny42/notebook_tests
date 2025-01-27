import logging

def setup_logger(name: str, log_file: str = "app.log", level: int = logging.INFO):
    """Set up a logger with options to choose the file and level."""
    logger = logging.getLogger(name)

    # If the logger already exists, avoid duplication
    if not logger.hasHandlers():
        handler = logging.FileHandler(log_file)  # Запись в файл
        handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        # Stream handler for logging to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
