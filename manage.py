#!/usr/bin/env python
import logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

import os
import sys

from platalert import get_current_version

if __name__ == '__main__':
    logger.info('Called manage.py')