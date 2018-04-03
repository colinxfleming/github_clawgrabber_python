from .github import fetch


class GithubClawgrabber():
    def __init__(self):
        pass

    def grab(self, repo, filepath, *helper_modules, branch='master'):
        github.fetch(auth_token, repo, filepath, branch)
        pass
