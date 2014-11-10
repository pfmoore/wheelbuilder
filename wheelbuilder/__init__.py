import click

@click.command()
@click.option('--project', help='Project to build.')
def main(project):
    """Simple program that builds a wheel for PROJECT."""
    pass
