from setuptools import setup, find_packages

setup(
    name='RankMyResume',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pdfminer.six',
        'scikit-learn',
        'pandas',
    ],
)