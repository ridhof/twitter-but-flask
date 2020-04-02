"""
Code module stores constant of Code and Message of each Code.
"""

OK = 0

DB_ERROR = 4001

PARAM_ERROR = 4101

AUTHORIZATION_ERROR = 4201

UNKNOWN_ERROR = 4301

CODE_MSG_MAP = {
    OK: 'ok',
    DB_ERROR: 'database error',
    PARAM_ERROR: 'request parameter error',
    AUTHORIZATION_ERROR: 'authentication and authorization erorr',
    UNKNOWN_ERROR: 'unknown error'
}
