from setuptools import find_packages, setup

setup ( 
    name = 'TextCollectionsLibrary', 
    packages = find_packages(), 
    version = '0.3.0', 
    description = 'Library to use the text collectins present in the article: "Benchmarking Text Collections for Classification and Clustering Tasks', 
    author = 'Marcos P. S. Gôlo',  
    install_requires = ['gdown']
)
