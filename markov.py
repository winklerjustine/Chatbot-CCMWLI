import sys
import collections
import random
import os

nonword = "\n"

class Markov():
    def __init__(self, order=2):
        self.order = order
        self.table = collections.defaultdict(list)
        self.seen = collections.deque([nonword] * self.order, self.order)
        self.poem = []

    def generate_table(self, filename):
        for line in open(filename):
            #print(line)
            for word in line.split():
                self.table[tuple(self.seen)].append(word)
                self.seen.append(word)
        self.table[tuple(self.seen)].append(nonword)

    def generate_output(self, max_words=100):
        self.seen.extend([nonword] * self.order)
        for i in range(max_words):
            word = random.choice(self.table[tuple(self.seen)])
            if word == nonword:
                exit()
            #print(word)
            self.poem.append(word)
            self.seen.append(word)
            poem = ' '.join(self.poem)
        print(poem)
        return poem

    def walk_directory(self, root_dir):
        for dir_name, sub_dir_list, file_list in os.walk(root_dir):
            print('Found directory: %s' % dir_name)
            for f_name in file_list:
                self.generate_table(os.path.join(dir_name, f_name))


#m = Markov(order=1)
#m.walk_directory('./shakespeare/love')
#m.generate_output(max_words=100)




