
import numpy as np
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from scipy import spatial
import nltk
nltk.download('punkt')

def compute_similarity(model, product_name1, product_name2):
    """
    Computes the cosine similarity between the embeddings of two product names using a pre-trained Word2Vec model.
    """
    # Tokenize the product names
    tokens1 = word_tokenize(product_name1)
    tokens2 = word_tokenize(product_name2)
    
    # Compute the embeddings for each product name
    embeddings1 = []
    for token in tokens1:
        if token in model.wv:
            embeddings1.append(model.wv[token])
    if not embeddings1:
        return 0.0
    embeddings1 = np.mean(embeddings1, axis=0)
    
    embeddings2 = []
    for token in tokens2:
        if token in model.wv:
            embeddings2.append(model.wv[token])
    if not embeddings2:
        return 0.0
    embeddings2 = np.mean(embeddings2, axis=0)
    
    # Compute the cosine similarity between the embeddings
    similarity = 1 - spatial.distance.cosine(embeddings1, embeddings2)
    
    return similarity
