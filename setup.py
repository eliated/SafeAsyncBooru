from setuptools import setup, find_packages

setup(
    name='SafeAsyncBooru',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'beautifulsoup4',
        'lxml'
    ],
    python_requires='>=3.6',
)