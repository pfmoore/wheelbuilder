from wheelbuilder import pypi

def test_getfiles():
    version, files = pypi.get('pip')
    assert version == '1.5.6'

def test_compat():
    assert pypi.has_compatible_wheel('pip')
    assert not pypi.has_compatible_wheel('pywin32')
