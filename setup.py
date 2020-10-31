import re
import ast

from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('preprocessing/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))
    setup(
        name='Project2',
        version=version,
        description='Import, preprocess and interpret EMG data for hand prosthesis',
        url='https://github.com/AlbertoMira/Project.git',
        license='MIT',
        author='Alberto Mira Criado, Johannes Payr',
        author_email=' ma8237@mci4me.at, j.payr@mci4me.at',
        platforms='any',

        packages=[
            'preprocessing'
        ],

        install_requires=[
            'numpy',
            'scipy',
            'click'
        ],

        entry_points='''
            [console_scripts]
            preprocess=preprocessing.main:main
        '''

    )

