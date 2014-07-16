"""
This module contains utility methods used by other parts of the
application.

"""
import re


def python_to_json_syntax(dict_to_convert):
    """
    Recursively update pythonic keys to JSON syntax in a dictionary
    and nested dictionaries if present.

    Args:
        dict_to_convert (dict): Dictionary with keys to convert from
            python to JSON syntax.

    """
    for key, value in dict_to_convert.iteritems():
        old_key = key
        for python_syntax in re.finditer(r'_[a-z]', key):
                key = key.replace(
                    python_syntax.group(), python_syntax.group()[1].upper())
        dict_to_convert[key] = dict_to_convert.pop(old_key)

        # Recursive call for nested dictionaries
        if type(value) == dict:
            python_to_json_syntax(value)