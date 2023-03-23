# Importing spacy
import spacy
from spacy.lang.fr.examples import sentences
# For regular expressions
import re
# For handling string
import string

# Loading model
nlp = spacy.load('fr_core_news_sm',disable=['parser', 'ner'])

def input_cleaning(product_name):
  #cleaning
  product_name=product_name.lower()
  product_name=re.sub('\w*\d\w*','', product_name)
  product_name=re.sub('[%s]' % re.escape(string.punctuation), '', product_name)
  product_name=re.sub(' +',' ',product_name)
  # Lemmatization with stopwords removal
  product_name = ' '.join([token.lemma_ for token in list(nlp(product_name)) if (token.is_stop==False)])
  return product_name
