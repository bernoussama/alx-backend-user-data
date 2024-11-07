#!/usr/bin/env python3
"""
    filtered logger
"""

import re


def filter_datum(fields, redaction, message, separator):
    """Filters a message for personal data"""
    for field in fields:
        message = re.sub(r"(?<={}=)[^;]*".format(field), redaction, message)
    return message
