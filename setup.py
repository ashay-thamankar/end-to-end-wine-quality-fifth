import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.5'

REPO_NAME = 'end-to-end-wine-quality-fifth'
AUTHOR_FULL_NAME = 'ashay-thamankar'
SRC_REPO = 'mlProject'
AUTHOR_EMAIL = 'ashaythamankar@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_FULL_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for ml project',
    long_description=long_description,
    long_description_content = 'text/markdown',
    url=f'https://github.com/{AUTHOR_FULL_NAME}/{REPO_NAME}',
    package_dir = {"": 'src'},
    packages=setuptools.find_packages(where='src')
)