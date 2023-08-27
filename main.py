from dotenv import load_dotenv
load_dotenv()

import logging.config
import os

if __name__ == '__main__':
    logging.config.fileConfig('config/logging_config.ini')
    log_level = os.environ.get('LOG_LEVEL', 'WARNING')
    logging.getLogger().setLevel(logging.getLevelName(log_level))

