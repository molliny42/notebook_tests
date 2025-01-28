import logging
import os

def setup_logger(name: str, log_file: str = "app.log", level: int = logging.INFO):
    """Set up a logger with options to choose the file and level."""
    # Ensure the logs directory exists
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)

    # Full path to the log file
    log_file_path = os.path.join(logs_dir, log_file)

    logger = logging.getLogger(name)

    # If the logger already exists, avoid duplication
    if not logger.hasHandlers():
        handler = logging.FileHandler(log_file_path)  # Save logs to a file
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
