from setuptools import setup, find_packages
from sys import path

path.insert(0, '.')

NAME = "logdna_line_export"

if __name__ == "__main__":
    setup(
        name=NAME,
        version="0.0.2",
        author="Jonathan Kelley",
        author_email="jonathan.kelley@logdna.com",
        url="https://github.com/jondkelley/logdna_line_export_cli",
        license='Copyleft',
        packages=find_packages(),
        package_dir={NAME: NAME},
        description="logdna_line_export - Just a simple webhook test app",
        include_package_data=True,
        install_requires=['Click','requests','python-dateutil'],

        entry_points={
            'console_scripts': ['logdna_line_export = logdna_line_export.main:entry'],
        }
    )
