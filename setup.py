from setuptools import setup

setup(
    name='ilprn',
    packages=['ilprn'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pymongo',
        'toolz',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
