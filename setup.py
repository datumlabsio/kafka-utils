from setuptools import setup, find_packages

setup(
    name='kutil',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'kmonitor = kutil.monitor:main'
        ]
    },
    author='Zain Ulabidin <zain@datumlabs.io>',
)