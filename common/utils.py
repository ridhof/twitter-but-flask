"""
Utils is a module that commonly used on many modules/components.
"""
from .code import CODE_MSG_MAP


def pretty_result(code, msg=None, data=None):
    """
    Pretty Result is a function to generate a pretty object from
    given code, message, and the data.
    """
    if msg is None:
        msg = CODE_MSG_MAP.get(code)
    return {
        'code': code,
        'msg': msg,
        'data': data
    }
