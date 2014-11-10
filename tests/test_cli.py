import click
from click.testing import CliRunner
from wheelbuilder import main

def test_help():
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert result.output != ''
