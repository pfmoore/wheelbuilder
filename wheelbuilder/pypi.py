import requests
from wheel.install import WheelFile

class PyPI:
    def __init__(self, project):
        url = 'https://pypi.python.org/pypi/{}/json'.format(project)
        req = requests.get(url)
        data = req.json()
        self.version = data['info']['version']
        self.files = data['releases'][self.version]

    def has_compatible_wheel(self):
        return any(WheelFile(obj['filename']).compatible for obj in self.files)
