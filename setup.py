from setuptools import setup, find_packages

setup(
    name='DNAdamageclassifierDx',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy', 'matplotlib', 'scikit-image', 'plotly'
    ],
    author='MD BABU MIA',
    author_email='md.babu.mia@mssm.edu',
    description='A package for analyzing DNA damage in COMET ASSAY images.',
    long_description=open('README.md').read(),
    url='https://github.com/yourusername/DNAdamageclassifierDx',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

