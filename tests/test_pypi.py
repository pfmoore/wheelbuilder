from wheelbuilder.pypi import PyPI

def test_getfiles():
    proj = PyPI('pip')
    assert proj.version == '1.5.6'

def test_compat():
    proj = PyPI('pip')
    assert proj.has_compatible_wheel()
    proj = PyPI('pywin32')
    assert not proj.has_compatible_wheel()
