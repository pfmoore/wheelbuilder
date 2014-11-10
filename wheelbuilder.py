import subprocess
import configparser
import os

py_versions = ('27','33', '34')
architectures = ('32', '64')

def python_homes():
    for py in py_versions:
        for arch in architectures:
            yield arch, 'C:\\Python{py}-{arch}'.format(py=py, arch=arch)

def normalize(name):
    """Convert project name to canonical PyPI form"""
    return name.lower().replace('_', '-')

def build_wheels(project, extras=None):
    env = os.environ.copy()
    project = normalize(project)
    tmpl = os.path.join('Config', '{}.cfg.template')
    template = None
    if os.path.exists(tmpl):
        home = os.path.abspath(os.curdir)
        env['HOME'] = home
        with open(tmpl) as f:
            template = f.read()

    for arch, pyhome in python_homes():
        if template:
            with open('pydistutils.cfg', 'w') as f:
                f.write(template.format(lib=os.path.join(home, 'Lib'),
                    arch=arch))
        python = os.path.join(pyhome, 'python.exe')
        cmd = [python, '-m', 'pip', 'wheel', '--no-deps', '--find-links', 'wheelhouse', '--wheel-dir', 'wheelhouse', project]
        print(cmd)
        subprocess.check_call(cmd, env=env)

def read_config(config):
    cp = configparser.ConfigParser(allow_no_value=True)
    cp.read(config)
    return cp

if __name__ == '__main__':
    cp = read_config('build.ini')
    for project in cp['projects']:
        build_wheels(project)
