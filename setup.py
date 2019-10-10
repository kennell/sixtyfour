from setuptools import setup, find_packages


setup(
    name='sixtyfour',
    version='1.0.0',
    package_dir={
        '': 'sixtyfour'
    },
    py_modules=['sixtyfour'],
    author='Kevin Kennell',
    author_email='kevin@kennell.de',
    license='MIT',
    url='https://github.com/kennell/sixtyfour',
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': [
            'sixtyfour = cli:main'
        ]
    }
)
