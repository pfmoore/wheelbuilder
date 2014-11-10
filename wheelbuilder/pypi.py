import requests
from wheel.install import WheelFile

def get(project):
    url = 'https://pypi.python.org/pypi/{}/json'.format(project)
    req = requests.get(url)
    data = req.json()
    ver = data['info']['version']
    files = data['releases'][ver]
    return ver, files

def has_compatible_wheel(project):
    ver, files = get(project)
    return any(WheelFile(obj['filename']).compatible for obj in files)
