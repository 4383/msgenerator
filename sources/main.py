__author__ = 'herve'
import json
import sys
import uuid
import requests
import yaml
import argparse
#token = '8ec5228887252e6ea53129a8869cfe9d62370c44'


def load_config(projectfile):
    #with open('project.yaml', 'r') as project:
    #    return yaml.load(project)
    return yaml.load(projectfile)


class Repo():
    data = None
    url = None
    template_url = None
    headers = None
    config = None

    def __init__(self, projectfile):
        self.config = load_config(projectfile)
        self.set_headers()
        self.log_headers()
        self.set_data()
        self.log_data()
        self.set_url()
        self.log_url()

    def set_headers(self):
        auth = self.config['repo']['auth']
        self.headers = {
            auth['header']: auth['token'],
            "Content-Type": "application/json",
        }

    def log_headers(self):
        print("Headers => {0}".format(self.headers))

    def set_data(self):
        self.data = json.dumps(self.config['project'])

    def log_data(self):
        print("Data => {0}".format(self.data))

    def set_url(self):
        self.url = self.config['repo']['url']
        self.template_url = self.config['template']['url']

    def log_url(self):
        print("Url => {0}".format(self.url))


def post(repo):
    r = requests.post(repo.url, data=repo.data, headers=repo.headers)
    return r.status_code, r


def init_repo(repo):
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
    #result = json.loads(result.text)
    print("Receive => {0}".format(status))
    print("Value => {0}".format(result.text))
    #if status != 201:
    #    print('Abort !!!!!')
    #    return
    init_repo(repo)


def ui(part):
    commands = {}
    for interaction, action in part.items():
        result = input(action)
        commands.update({interaction: result})
    return commands


def generate():
    print("-"*25)
    print("Action generate")
    print("-"*25)
    ui_repo = {"type": "type <github|gitlab> = ", "url": "url = ",}
    ui_auth = {"token": "token = ", "header": "header = "}
    ui_project = {"name": "name = ", "description": "description = " }
    repo = {} 
    repo.update(ui(ui_repo))
    auth = {}
    auth.update(ui(ui_auth))
    project = {}
    project.update(ui(ui_project))
    save(repo, auth, project)


def write(output, item, tabspace=4):
    for interaction, action in item.items():
        tabultation = " "*tabspace
        output.write("{0}{1}: {2}\n".format(tabultation, interaction, action))


def save(repo, auth, project):
    filename = input("Specify projectfile name : ")
    with open("{0}.yaml".format(filename), 'w+') as output:
        output.write("repo:\n")
        write(output, repo)
        output.write("    auth:\n")
        write(output, auth, tabspace=8)
        output.write("project:\n")
        write(output, project)


def orchestrat():
    print(args().cpf)
    if not args().cpf:
        create()
        return
    generate()


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cpf', 
                        help="Create an initialized project file",
                        type=str, 
                        default=None)
    parser.add_argument('--projectfile', 
                        help="The project file to create",
                        type=argparse.FileType('r'), 
                        default=sys.stdin)
    return parser.parse_args()


if __name__ == '__main__':
    orchestrat()
