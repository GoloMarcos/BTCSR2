# BTCSR2
Library to use the text collectins present in the article: Benchmarking Text Collections for Classification and Clustering Tasks

# To use

!pip install git+https://github.com/GoloMarcos/BTCSR2/

from TextCollectionsLibrary import datasets

datasets_dictionary = datasets.load()

dataset_dictionaty[base name] return a DataFrame

# The DataFrame have the columns
- Text
- Embedding from BERT
- Embedding from DistilBERT
- Embeddings from Multilingual DistilBERT 
- Embedding from RoBERTa
- Class of the documents
