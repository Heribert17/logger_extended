"""
Test the logger
"""

import os
from context import logger_extended  # pylint: disable=import-error

mylogger = logger_extended.logger.Logger(
    os.path.join(os.path.dirname(__file__), "Logfile.log"), console=False, memory=True
)
for i in range(100000):
    mylogger.info("Info message\n   with two lines.")
    mylogger.error("ERROR")
    if i % 10000 == 0:
        print(i)
