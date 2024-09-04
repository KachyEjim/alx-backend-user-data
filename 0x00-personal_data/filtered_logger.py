#!/usr/bin/env python3
"""Python file"""
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """Before an obfucation on a message"""

    pattern = "|".join([f"{field}=[^{separator}]+" for field in fields])
    return re.sub(
        pattern, lambda m: m.group(0).split("=")[0] + "=" + redaction, message
    )




class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, field: list):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError