import os

from setuptools import setup

version = "1.0.1"

# here - where we are.
here = os.path.abspath(os.path.dirname(__file__))

# read the package requirements for install_requires
with open(os.path.join(here, 'requirements.txt'), 'r') as f:
    requirements = f.readlines()

# setup!
setup(
    name='cvestream',

    author='Leon Jacobs',
    author_email='leonja511@gmail.com',

    description='a small utility to dump NVD information',
    license='GPL v3',
    packages=['cvestream'],
    install_requires=requirements,
    python_requires='>=3.5',

    url='https://github.com/leonjza/cvestream',
    download_url='https://github.com/leonjza/cvestream/archive/' + version + '.tar.gz',

    keywords=['docker', 'tool', 'pentest', 'framework'],
    version=version,

    classifiers=[
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
    ],
    entry_points={
        'console_scripts': [
            'cvestream = cvestream.main:main',
        ],
    },
)
