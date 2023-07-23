"""
Test the logger
"""

import os
from context import logger_extended  # pylint: disable=import-error

logfile = os.path.join(os.path.dirname(__file__), "Logfile.log")
if os.path.exists(logfile):
    os.remove(logfile)
mylogger = logger_extended.logger.Logger(
    logfile, console=False, memory=True
)
for i in range(1000):
    mylogger.info("Info message\n   with two lines.")
    mylogger.error("ERROR")
    mylogger.set_debug(True)
    mylogger.debug("Debug should be in log")
    mylogger.set_debug(False)
    mylogger.debug("Debug should not be in log")
