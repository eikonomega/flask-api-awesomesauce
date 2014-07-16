"""
Custom Exceptions

"""


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class MalformedJson(Error):
    """
    Exception raised for errors in JSON strings.

    """
    pass