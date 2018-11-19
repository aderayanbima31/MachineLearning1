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
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def response(user_response):
    robo_response = ''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat [-2]
    if(req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response




flag = True
print "ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!"
while(flag == True):
    user_response = raw_input()
    user_response = user_response.lower()
    if(user_response != 'bye'):
        if(user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print "ROBO: You are welcome..."

        else:
            if(greeting(user_response) != None):
                print "ROBO : " + greeting(user_response)
            else:
                sent_tokens.append(user_response)
                word_tokens = word_tokens + nltk.word_tokenize(user_response)
                final_words = list(set(word_tokens))
                print "ROBO:"
                print response(user_response)
                sent_tokens.remove(user_response)

    else:
        flag = False
        print "ROBO : Bye! take care.."


