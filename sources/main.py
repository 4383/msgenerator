__author__ = 'herve'
import json
import sys
import uuid
import argparse
from core.create import create
from core.generate import generate
from core.repository import Repo
from core.ui import splash


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
    splash()
    orchestrat()
