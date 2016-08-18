import argparse
import sys
import sources.commands.create as cmd_create
import sources.commands.generate as cmd_generate
import sources.commands.search as cmd_search
import sources.commands.pull as cmd_pull
__version__="0.1"


class MicroService(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
        description='Micro Service Generator',
        usage='''msgenerator <command> [<args>]
        
The most commonly used git commands are:
    commit     Record changes to the repository
    fetch      Download objects and refs from another repository
        ''')
        epilogue='''Credits :
        
author: Hervé Beraud
version: {0}
        '''.format(__version__)
        parser.add_argument('command', help='Subcommand to run')
        parser.add_argument('--version', help='Print version', action='version', version='microservice version {version}'.format(version=__version__))
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()
        
    def create(self):
        cmd_create.run()

    def generate(self):
        cmd_generate.run()

    def search(self):
        cmd_search.run()

    def pull(self):
        cmd_pull.run()


if __name__ == "__main__":
    MicroService()
