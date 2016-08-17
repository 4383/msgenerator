import json
import yaml


def load_config(projectfile):
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

