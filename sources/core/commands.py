import sys
import pkgutil

__all__ = []


class Commands(list):
    def __init__(self):
        list.__init__(self)
        self.load()

    def load(self):
        for importer, modname, ispkg in pkgutil.iter_modules(commands.__path__):
            if not ispkg:
                self.append(modname)
                __all__.append(modname)

    def execute(self, name, domain, limit, proxy, user_agent):
        return self.run(name, domain, limit, proxy, user_agent)

    def run(self, name, domain, limit, proxy, user_agent):
        commands_path = "sources.commands.{0}".format(name)
        module = __import__(commands_path, globals(), locals(), ['object'], 0)
        return module.start()
