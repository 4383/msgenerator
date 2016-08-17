import requests


def post(repo):
    r = requests.post(repo.url, data=repo.data, headers=repo.headers)
    return r.status_code, r


def initialize(repo):
    from subprocess import call
    print('git ', 'clone ', repo.template_url)
    call(['git', 'clone', repo.template_url])
    pass


def create():
    print("-"*25)
    print("Action create")
    print("-"*25)
    repo = Repo(args().projectfile)
    status, result = post(repo)
    print("Receive => {0}".format(status))
    print("Value => {0}".format(result.text))
    if status != 201:
        print('Abort !!!!!')
        return
    initialize(repo)

