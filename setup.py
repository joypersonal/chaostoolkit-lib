#!/usr/bin/env python
"""chaostoolkit core library builder and installer"""

import sys
import io

import setuptools

sys.path.insert(0, ".")
from chaoslib import __version__
sys.path.remove(".")

name = 'chaostoolkit-lib'
desc = 'Chaos engineering toolkit core library'

with io.open('README.md', encoding='utf-8') as strm:
    long_desc = strm.read()

classifiers = [
    'Development Status :: 2 - Pre-Alpha',  
    'Intended Audience :: Developers',
    'License :: Freely Distributable',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation',
    'Programming Language :: Python :: Implementation :: CPython',
    'Topic :: System :: Distributed Computing'
]
author = 'chaostoolkit Team'
author_email = 'contact@chaostoolkit.org'
url = 'http://chaostoolkit.org'
license = 'Apache License Version 2.0'
packages = [
    'chaoslib',
    'chaoslib.discovery',
    'chaoslib.provider'
]

needs_pytest = set(['pytest', 'test']).intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
test_require = []
with io.open('requirements-dev.txt') as f:
    test_require = [l.strip() for l in f if not l.startswith('#')]

install_require = []
with io.open('requirements.txt') as f:
    install_require = [l.strip() for l in f if not l.startswith('#')]

extras_require = {
    "vault": [
        "ply==3.4",
        "pyhcl>=0.2.1,<0.3.0",
        "hvac"
    ]
}

setup_params = dict(
    name=name,
    version=__version__,
    description=desc,
    long_description=long_desc,
    classifiers=classifiers,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    packages=packages,
    include_package_data=True,
    install_requires=install_require,
    tests_require=test_require,
    setup_requires=pytest_runner,
    extras_require=extras_require,
    python_requires='>=3.5.*'
)


def main():
    """Package installation entry point."""
    setuptools.setup(**setup_params)


if __name__ == '__main__':
    main()
