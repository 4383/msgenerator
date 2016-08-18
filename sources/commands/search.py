import argparse
import sys
import requests
from sources.core.ui import ui, Colors
from sources.core.ui import success, warning, info
from sources.core.ui import search as display

OFFICIAL_REPO_URL='https://api.github.com/users/microservice/repos'

class Research:

    def __init__(self, name, url=OFFICIAL_REPO_URL):
        self.url = url
        self.name = name

def load(url):
    info("Fetching {0} repository".format(url))
    r = requests.get(url)
    if r.status_code >= 300:
        print('Loading results fail ({0}) !\n{1}'.format(r.status_code, r.json()))

    return r.json()


def search(symbols, message=None):
    if type(symbols) != Research:
        warning("Wrong research object")
        exit(1)
    data = load(symbols.url)
    for project in data:
        if project['name'] == symbols.name:
            if not message:
                display(project['name'], project['description'])
            else:
                success(message)
            return project
    warning("No results found !")
    exit(1)


def get(symbols):
    search(symbols, "Project found !")


def run():
    parser = argparse.ArgumentParser(
    description='Search project skeleton')
    parser.add_argument('name', help='Skeleton name')
    parser.add_argument('--repo', help='Remote repository url', 
                            default=OFFICIAL_REPO_URL)
    parser.add_argument('--verbose', 
                            help="Activate verbose mode",
                            choices=('on', 'off'),
                            default='off')

    args = parser.parse_args(sys.argv[2:])
    if args.verbose == 'on':
        args.verbose = True
    else:
        args.verbose = False
    symbols = Research(args.name, args.repo)
    search(symbols)
