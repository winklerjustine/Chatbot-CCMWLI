import numpy as np
from nltk.corpus import stopwords
from gensim.scripts.glove2word2vec import glove2word2vec

glove_input_file = 'glove.6B.50d.txt'
word2vec_output_file = 'glove.6B.50d.txt.word2vec'
glove2word2vec(glove_input_file, word2vec_output_file)

from gensim.models import KeyedVectors
import xlrd
# load the Stanford GloVe model
filename = 'glove.6B.50d.txt.word2vec'
model = KeyedVectors.load_word2vec_format(filename, binary=False)

def calc_similarity(key_string, message_string):
    sim = []
    for word1 in key_string:
        for word2 in message_string:
            sim.append(model.similarity(word1, word2))
    mean = np.mean(sim)
    return mean

#calc_similarity(['hello', 'hey', 'hi', 'hallo', 'hoi', 'greetings', 'day', 'morning', 'afternoon', 'evening'], ['hello', 'how', 'are', 'you'])
#calc_similarity(['how', 'going', 'doing', 'what', 'up', 'sup'], ['hello', 'how', 'are', 'you'])