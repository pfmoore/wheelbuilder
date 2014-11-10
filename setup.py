from setuptools import setup

setup(
    name="wheelbuilder",
    version='0.1',
    description="Generate wheels for PyPI packages",
    long_description="Generate wheels for PyPI packages",

    url='http://github.com/pfmoore/wheelbuilder',

    author='Paul Moore',
    author_email='p.f.moore@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        # Consider adding Python 2 support later...
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='packaging development',
    packages=['wheelbuilder'],
    install_requires = ['requests', 'click'],
    entry_points={
        'console_scripts': [
            'wheelbuilder=wheelbuilder:main',
        ],
    },
)
