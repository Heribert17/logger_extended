"""
Set context to access logger module.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)

import logger_extended.logger  # pylint: disable=unused-import,wrong-import-position,import-error
