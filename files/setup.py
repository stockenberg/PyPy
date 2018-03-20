from setuptools import setup

setup(
    name="mom",
    version="0.1",
    description="learn by doin",
    entry_points={
        'console_scripts': [
            'mom=mom.generator:main'
        ]
    },
    packages=['mom']
)

__author__ = "Marten Stockenberg"