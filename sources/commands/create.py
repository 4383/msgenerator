import argparse
import json
import sys
import requests
from sources.core.repository import Repo


def post(repo):
    r = requests.post(repo.url, data=repo.data, headers=repo.headers)
    return r.status_code, r


def initialize(repo):
    from subprocess import call
    print('git ', 'clone ', repo.template_url)
    call(['git', 'clone', repo.template_url])
    pass


def create(args):
    repo = Repo(
            verbose=args.verbose,
            projectfile=args.config
    )
    status, result = post(repo)
    result = result.json()
    if status != 201:
        print('Failed ({0}) to create a new remote repository !'.format(status))
        print(result['message'])
        return
    initialize(repo)


def run():
    parser = argparse.ArgumentParser(
    description='Generate a new virgin project from template')
    parser.add_argument('--config', 
                            help="Microservice configuration file",
                            type=argparse.FileType('r'), 
                            default='Microservice')

    parser.add_argument('--verbose', 
                            help="Activate verbose mode",
                            choices=('on', 'off'),
                            default='off')

    args = parser.parse_args(sys.argv[2:])
    if args.verbose == 'on':
        args.verbose = True
    else:
        args.verbose = False
    create(args)
