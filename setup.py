from setuptools import setup, find_packages
from sys import path

from answerbook_webhook_test import __version__

path.insert(0, '.')

NAME = "logdna_line_export"

if __name__ == "__main__":
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

    setup(
        name=NAME,
        version=__version__,
        author="Jonathan Kelley",
        author_email="jonathan.kelley@logdna.com",
        url="https://github.com/jondkelley/logdna_line_export_cli",
        license='Copyleft',
        packages=find_packages(),
        package_dir={NAME: NAME},
        description="logdna_line_export - Just a simple webhook test app",

        install_requires=requirements,

        entry_points={
            'console_scripts': ['logdna_line_export = logdna_line_export.main:entry'],
        }
    )
