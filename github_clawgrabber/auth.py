"""Load authentication token."""

import os

__all__ = ['auth_token']


def auth_token(token=None):
    """Use the passed in token or take it from fallbacks."""
    auth_token = token or from_environ()
    if not auth_token:
        raise NoAuthenticationTokenError(ERROR_MSG)
    return auth_token


def from_environ():
    """OS calls are ugly, so delegate this to its own func."""
    return os.environ.get('GITHUB_API_TOKEN', None)


ERROR_MSG = ('GitHub auth token not found. Either pass one in as an argument, '
             'or set one in environment at GITHUB_API_TOKEN.')


class NoAuthenticationTokenError(TypeError):
    pass
