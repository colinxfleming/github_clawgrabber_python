# Github Clawgrabber... in Python

This is a utility that fetches a file from Github, templates it according to
the rules set up, 

Works great with:

See [the ruby version](https://github.com/colinxfleming/github_clawgrabber_ruby)
for the original implementation. I'll try and keep them both up to speed, but no
promises, as I am but one person, etc.

## Installing

TK

## Usage

### In another python app or script

```python
import github_clawgrabber

github_clawgrabber.grab(auth_token, repo, filepath, branch = 'master', *modules)

# ex
github_clawgrabber.grab('12345',
						'colinxfleming/github_clawgrabber_python',
						'sample/does_it_blend.sql.mako')
```

### As a CLI

```shell
# assign your github env vars, so the api call doesn't fail
github_clawgrabber git_user/repo path_to_file --args

# ex:
export GITHUB_CLAWGRABBER_TOKEN=1234567890
github_clawgrabber colinxfleming/github_clawgrabber_python sample/does_it_blend.sql.mako
```

## Project setup

```sh
git clone git@github.com:colinxfleming/github_python_clawgrabber
pyenv install 3.6.4
source setup.sh
```

### Running tests

```sh
pytest
```

## A note about Mako, the templating language used here

This uses [mako](http://docs.makotemplates.org/) instead of jinja2 because it's
closer to raw python. Tag templatable files with `.mako` at the end to more
clearly identify them -- e.g. `reports.sql.mako`.
