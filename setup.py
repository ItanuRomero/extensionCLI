from setuptools import setup
setup(
    name = 'extension',
    version = '0.1.0',
    packages = ['extension'],
    entry_points = {
        'console_scripts': [
            'ext = extension.__main__:main'
        ]
    })