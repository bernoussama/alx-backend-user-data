#!/usr/bin/env python3
"""
    filtered logger
"""

import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
):
    """Filters a message for personal data"""
    for field in fields:
        message = re.sub(r"(?<={}=)[^;]*".format(field), redaction, message)
    return message
