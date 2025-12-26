"""
Simplified logger module for python

Author: Heribert Füchtenhans

Version: 2025.12.26

Implements a rolling file logger that also is able to output to console and
save all logging output in memory, so that it can be retrieved.
The logger handles multiline messages correctly and splits it into multiple
lines.
"""

import io
import logging
import logging.handlers
import os
import sys
from typing import final

# ------------------------------------------------------------------------------------------------


@final
class Logger:
    """
    Logger that logs multiline text correctly.
    """

    def __init__(
        self,
        logfilename: str,
        debuging: bool = False,
        console: bool = True,
        memory: bool = False,
        logfilesize: int = 10_000_000,
    ) -> None:
        """
        Sets the logging for file output, console and memory
        logfile: Name of the logfile, may include path
        debuging: if True debugging information will also be written
        console: if True output will also be send to the console
        memory: if True output will be saved in memory and can be retrieved
        """
        self._log_console = None
        self._log_memory = None
        self._memory = None
        self._loglevel = logging.DEBUG if debuging else logging.INFO
        self._logging = logging.getLogger("Log")
        self._logging.setLevel(self._loglevel)
        logformat = "%(levelname)-7s %(asctime)s: %(message)s"
        # Output to console
        if console:
            self._log_console = logging.StreamHandler(sys.stdout)
            self._log_console.setLevel(self._loglevel)
            self._log_console.setFormatter(logging.Formatter(logformat))
            self._logging.addHandler(self._log_console)
        if memory:
            # output to memory
            self._memory = io.StringIO()
            self._log_memory = logging.StreamHandler(self._memory)
            self._log_memory.setLevel(self._loglevel)
            self._log_memory.setFormatter(logging.Formatter(logformat))
            self._logging.addHandler(self._log_memory)
        # output to file
        outpath = os.path.dirname(logfilename)
        if outpath != "":
            os.makedirs(outpath, exist_ok=True)
        self._log_file = logging.handlers.RotatingFileHandler(
            logfilename, "a", logfilesize, 5, delay=True, encoding="UTF-8"
        )
        self._log_file.setLevel(self._loglevel)
        self._log_file.setFormatter(logging.Formatter(logformat))
        # Check if we should do a rollover when we already reached 90 % filling
        if os.path.getsize(logfilename) > int(logfilesize * 0.9):
            self._log_file.doRollover()
        self._logging.addHandler(self._log_file)

    def info(self, text: str) -> None:
        """Log info message"""
        for line in text.split("\n"):
            self._logging.info(line.rstrip())

    def warning(self, text: str) -> None:
        """Log warning message"""
        for line in text.split("\n"):
            self._logging.warning(line.rstrip())

    def error(self, text: str) -> None:
        """Log error message"""
        for line in text.split("\n"):
            self._logging.error(line.rstrip())

    def debug(self, text: str) -> None:
        """Log debug message"""
        if self._loglevel != logging.DEBUG or text == "":
            return
        for line in text.split("\n"):
            self._logging.debug(line.rstrip())

    def exception(self, text: str) -> None:
        """Log exception"""
        for line in text.split("\n"):
            self._logging.exception(line.rstrip())

    def set_debug(self, activate: bool = True) -> None:
        """Set debug loglevel on or off"""
        self._loglevel = logging.DEBUG if activate else logging.INFO
        self._log_file.setLevel(self._loglevel)
        if self._log_console:
            self._log_console.setLevel(self._loglevel)
        self._logging.setLevel(self._loglevel)
        if self._log_memory:
            self._log_memory.setLevel(self._loglevel)

    def get_saved_log(self) -> str:
        """get the in memory saved logging messages."""
        return self._memory.getvalue() if self._memory else ""

    def get_filelogger(self) -> logging.Logger:
        """return the used Python file logger"""
        return self._logging
