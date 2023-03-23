
import pandas as pd
from gensim.models import Word2Vec
from compute_similarity import compute_similarity

# Load the product metadata CSV file
data = pd.read_csv('data/cleanData.csv')

# Load the model
model = Word2Vec.load("models/word2vec.model")

def get_similar_products(product_name, n):
    # Compute the semantic similarity between the given product name and all other product names
    similarities = []
    for name in data['name']:
        similarity = compute_similarity(model, product_name, name)
        similarities.append(similarity)
    
    # Sort the products by semantic similarity
    data['similarity'] = similarities
    df_sorted = data.sort_values(by='similarity', ascending=False)
    
    # Get the n most and least similar products
    most_similar = df_sorted.head(n)[['name', 'brand', 'category', 'similarity']]
    least_similar = df_sorted.tail(n)[['name', 'brand', 'category', 'similarity']]
    
    return most_similar, least_similar
