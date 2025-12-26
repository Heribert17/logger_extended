# logger_extened

Implements a rolling file logger that also is able to output to console and
save all logging output in memory, so that it can be retrieved.
The logger handles multiline messages correctly and splits it into multiple
lines.

For detailed description see (https://heribert17.github.io/logger_extended/)

Tested with:
* Python 3.10 and above

# Changelog
* 1.0.0
    * Initial version
* 1.0.1
    * Debug logging optimized if debug isn't active
* 1.0.2
    * Do a rollover of the logfile if we have already reached 90% if filling when initialisizing the logger

