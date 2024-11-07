#!/usr/bin/env python3
"""
    filtered logger
"""

import re
from typing import List
import logging

patterns = {
    "extract": lambda a, b: r"(?P<field>{})=[^{}]*".format("|".join(a), b),
    "replace": lambda a: r"\g<field>={}".format(a),
}


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Filters a message for personal data"""
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats a record"""
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR
        )
