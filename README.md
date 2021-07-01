# Bechmarking of text collections from Solange, Ricardo and Rafael (BTCSR2)

# TextCollectionsLibrary
Library to use the text collectins present in the article: Benchmarking Text Collections for Classification and Clustering Tasks. The article are avaliable at "http://repositorio.icmc.usp.br/bitstream/handle/RIICMC/6641/Relat%C3%B3rios%20T%C3%A9cnicas_395_2013.pdf?sequence=1"

# How To use

!pip install git+https://github.com/GoloMarcos/BTCSR2/

from TextCollectionsLibrary import datasets

datasets_dictionary = datasets.load()

dataset_dictionaty[base name] return a DataFrame

# Datasets
- CSTR
- Classic4
- SiskillWebert
- Webkb-parsed
- Review_polarity
- Re8
- NSF
- indrustry Sector
- Dmoz-Sports
- Dmoz-Science
- Dmoz-Health
- Dmoz-Computers


# Columns from DataFrame
- Text
- Embedding from BERT
- Embedding from DistilBERT
- Embeddings from Multilingual DistilBERT 
- Embedding from RoBERTa
- Document class

# We obtain the embeddings with the library sentence_tranformers
- BERT model: bert-large-nli-stsb-mean-tokens
  -  Devlin, Jacob, et al. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers). 2019.
- DistilBERT model: distilbert-base-nli-stsb-mean-tokens
  -  Sanh, Victor, et al. "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter." arXiv preprint arXiv:1910.01108 (2019).
- RoBERTa model: roberta-large-nli-stsb-mean-tokens
  - Liu, Yinhan, et al. "Roberta: A robustly optimized bert pretraining approach." arXiv preprint arXiv:1907.11692 (2019).
- DistilBERT Multilingual model: distiluse-base-multilingual-cased
  - Sanh, Victor, et al. "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter." arXiv preprint arXiv:1910.01108 (2019).
