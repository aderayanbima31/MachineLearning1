import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer #library for TFidf
from sklearn.metrics.pairwise import  cosine_similarity #

f = open('chatbot.txt', 'r')
raw = f.read()
raw = raw.lower() #convert to lowercase


sent_tokens = nltk.sent_tokenize(raw) #convert to list of sentensce
word_tokens = nltk.word_tokenize(raw) #convert to list of words

print sent_tokens[:2]
print word_tokens[:2]


#Prepocessing the raw text
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):

    return [lemmer.lemmatize(token) for token in tokens]
remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))


#Keyword Matching
GREETINGS_INPUTS = ('hello', 'hi', 'greetings', '')