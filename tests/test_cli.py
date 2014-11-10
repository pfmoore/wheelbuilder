import click
from click.testing import CliRunner
from wheelbuilder import main, __version__

def test_help():
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert result.output != ''

def test_version():
    runner = CliRunner()
    result = runner.invoke(main, ['--version'])
    assert result.exit_code == 0
    assert __version__ in result.output

def test_project_arg():
    runner = CliRunner()
    result = runner.invoke(main, ['pip'])
    assert result.exit_code == 0

def test_multiple_projects():
    runner = CliRunner()
    result = runner.invoke(main, ['pip', 'setuptools'])
    assert result.exit_code == 0

def test_file_arg():
    runner = CliRunner()
    result = runner.invoke(main, ['--file', 'projects.txt'])
    assert result.exit_code == 0
