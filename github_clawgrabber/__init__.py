from .github import fetch
from .auth import auth_token


def grab(repo, filepath, token=None, *helper_modules, branch='master'):
    fetched = fetch(repo, filepath, branch, auth_token(token))
    return fetched
