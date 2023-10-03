from setuptools import setup, find_packages

setup(
    name='RankMyResume',
    version='1.4.0',
    description='Rank you resume based on job description',
    packages=find_packages(),
    install_requires=[
        'pdfminer.six',
        'scikit-learn',
        'pandas',
    ],
)