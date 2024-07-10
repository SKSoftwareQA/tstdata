import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Ensure the Logs directory exists
        log_directory = "./Logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Create a custom logger
        logger = logging.getLogger("automation_logger")
        logger.setLevel(logging.INFO)

        # Create handlers
        log_file = os.path.join(log_directory, "automation.log")
        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()  # Optional: Add console logging

        # Create formatters and add them to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)  # Optional: Set console formatter

        # Add handlers to the logger
        if not logger.handlers:  # Prevent adding multiple handlers if loggen() is called multiple times
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)  # Optional: Add console handler

        return logger
