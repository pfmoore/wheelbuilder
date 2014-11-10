import click

__version__ = '0.1'

@click.command()
@click.version_option(version=__version__)
@click.argument('project', nargs=-1)
@click.option('--file', help="A file containing projects to build")
def main(project, file):
    """Simple program that builds a wheel for PROJECT."""
    pass
