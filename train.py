
import pandas as pd
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

# Load the product metadata CSV file
data = pd.read_csv('data/cleanData.csv')

# Tokenize the product names
tokenized_names = data['name'].apply(word_tokenize)

# Train a Word2Vec model on the tokenized product names
model = Word2Vec(tokenized_names,min_count=1, workers=4)

model.save("models/word2vec.model")
