# Bechmarking of text collections from Solange, Ricardo and Rafael (BTCSR2)

# TextCollectionsLibrary
Library to use the text collectins present in the article: Benchmarking Text Collections for Classification and Clustering Tasks. The article are avaliable at "http://repositorio.icmc.usp.br/bitstream/handle/RIICMC/6641/Relat%C3%B3rios%20T%C3%A9cnicas_395_2013.pdf?sequence=1"

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
- Document class
