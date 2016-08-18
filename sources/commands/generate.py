import argparse
import sys
from sources.core.ui import ui

def generate(args):
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
    save(repo, auth, project, args.file)


def write(output, item, tabspace=4):
    for interaction, action in item.items():
        tabultation = " "*tabspace
        output.write("{0}{1}: {2}\n".format(tabultation, interaction, action))


def save(repo, auth, project, output):
    output.write("repo:\n")
    write(output, repo)
    output.write("    auth:\n")
    write(output, auth, tabspace=8)
    output.write("project:\n")
    write(output, project)

def run():
    parser = argparse.ArgumentParser(
    description='Create a new intialized project from template')
    parser.add_argument('--name', help='Project name')
    parser.add_argument('--token', help='Project name')
    parser.add_argument('--description', help='Project name')
    parser.add_argument('--header', help='Project name')
    parser.add_argument('--type', help='Project name', choices=('github', 'gitlab', 'bitbucket'))
    parser.add_argument('--url', help='Project name')
    parser.add_argument('--file', help='Generated output file, default "Microservice"',type=argparse.FileType('w+'), default='Microservice')
    parser.add_argument('--verbose', 
                            help="Activate verbose mode",
                            choices=('on', 'off'),
                            default='off')

    args = parser.parse_args(sys.argv[2:])
    if args.verbose == 'on':
        args.verbose = True
    else:
        args.verbose = False
    generate(args)
