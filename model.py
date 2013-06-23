from gensim import corpora, models, similarities
#import MyCorpus
import glob

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO,filename="staatsblad_topics100_len3_tfidf_5.txt")

"""
dictionary = corpora.dictionary.Dictionary()
new_doc = ["Human", "computer", "interaction"]
new_vec = dictionary.doc2bow(new_doc,allow_update=True)
print new_vec
print new_vec.token2id
print new_vec.doc2bow()
raw_input()
"""

class MyCorpus(object):
    def __iter__(self):

        for f in glob.glob('articles/frog/*'):
            text = []
            i = open(f)
            for line in i:
                line = line.strip().split("\t")
                if len(line) > 2:
                    word = line[2].lower()
                    if len(word) > 2 and not stop.has_key(word):
                        text.append(word)
            i.close()
            yield dictionary.doc2bow(text,allow_update=True)


def readStopWords():
    stop = {}
    i = open('dutch-stop-words.txt')
    for x in i.readlines():
        stop[x.strip()] = 1
    i.close()
    return stop

stop = readStopWords()

dictionary = corpora.dictionary.Dictionary()
corpus = MyCorpus()

#for vector in corpus:
#    print vector
 
print "Normalization"   
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

print "Modeling"
#lsi = models.LsiModel(corpus_tfidf,id2word = dictionary, num_topics = 100)
#lsi.show_topics()

model = models.ldamodel.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=100)
model.show_topics(topics=-1,topn=100,log=True)
