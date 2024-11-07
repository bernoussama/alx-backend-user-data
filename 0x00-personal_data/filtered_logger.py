#!/usr/bin/env python3
"""
    filtered logger
"""

import re
from typing import List

patterns = {
    "eatract": lambda a, b: r"(?P<field>{})=[^{}]*".format("|".join(a), b),
    "replace": lambda a: r"\g<field>={}".format(a),
}


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Filters a message for personal data"""
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
