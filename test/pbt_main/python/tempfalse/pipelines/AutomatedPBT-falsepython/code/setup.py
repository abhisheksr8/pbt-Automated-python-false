from setuptools import setup, find_packages

setup(
    name='AutomatedPBT-falsepython',
    version='1.0',
    packages=find_packages(include=['automatedpbtfalsepython*']),
    description='AutomatedPBT-falsepython',
    install_requires=[
        'prophecy-libs==1.6.9'
    ],
    entry_points={
        'console_scripts': [
            'main = automatedpbtfalsepython.pipeline:main',
        ],
    },
    data_files=[(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require={
        'test': ['pytest', 'pytest-html'],
    }
)