# GloVe trained on Wikipedia
# http://nlp.stanford.edu/data/glove.6B.zip

# re-save pretrained GloVe in word2vec format
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = 'glove.6B.100.txt'
word2vec_output_file = 'glove.6B.100d.txt.word2vec'
glove2word2vec(glove_input_file, word2vec_output_file)

from gensim.models import KeyedVectors
# load the Stanford GloVe model
filename = 'glove.6B.100d.txt.word2vec'
model = KeyedVectors.load_word2vec_format(filename, binary=False)
# calculate: (king - man) + woman = ?
result = model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
print(result)