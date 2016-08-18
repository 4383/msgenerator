import argparse
import sys
from sources.core.ui import description


class Args():
    __instance = None

    def __new__(cls):
        if Args.__instance is None:
            Args.__instance = object.__new__(cls)
        return Args.__instance


    def __init__(self):
        parser = argparse.ArgumentParser()
        #parser.add_argument('command',
        #                    help='Command to use')
        parser.add_argument('--cpf', 
                            help="Create an initialized project file",
                            type=str, 
                            default=None)
        parser.add_argument('--projectfile', 
                            help="The project file to create",
                            type=argparse.FileType('r'), 
                            default=sys.stdin)
        self.args = parser.parse_args()


    def get(self):
        pass
        #if not self.parser.parse_args():
        #    self.parser.print_help()
        #return self.parser.parse_args()
