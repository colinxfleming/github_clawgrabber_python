"""Handle github interactions."""

import requests
import json

__all__ = ['fetch', 'GITHUB_GRAPHQL_ENDPOINT']

GITHUB_GRAPHQL_ENDPOINT = 'https://api.github.com/graphql'


def fetch(auth_token, repo, filepath, branch):
    headers = _define_headers(auth_token)
    query_json = _shape_graph_query(repo, filepath, branch)
    result = requests.post(
        GITHUB_GRAPHQL_ENDPOINT,
        data=query_json,
        headers=headers)

    result.raise_for_status()
    # return result

    return _reduce(filepath, result)


def _define_headers(auth_token):
    return {'Authorization': "bearer {}".format(auth_token),
            'User-Agent': 'github_clawgrabber_python'}


def _shape_graph_query(repo, filepath, branch):
    repository = 'repository(owner: "{0}", name: "{1}")'.format(
        repo.split('/')[0], repo.split('/')[1])
    content = 'object(expression: "{0}:{1}")'.format(branch, filepath)
    req_json = "query {{ {0} {{ {1} {{ ... on Blob {{ text }} }} }} }}".format(
        repository, content)

    return json.dumps({'query': req_json})


def _reduce(filepath, response):
    raw = json.loads(response.content)['data']['repository']['object']['text']
    return [{'filepath': filepath, 'content': raw}]
