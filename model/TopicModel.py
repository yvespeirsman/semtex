from gensim import corpora, models, similarities
import logging

class MyCorpus(object):

    def __init__(self,listOfFiles,stopList={}):
        self.files = listOfFiles
        self.stop = stopList
        self.dictionary = corpora.dictionary.Dictionary()

    def __iter__(self):

        for f in self.files:
            text = []
            i = open(f)
            for line in i:
                line = line.strip().split("\t")
                if len(line) > 2:
                    word = line[2].lower()
                    if len(word) > 2 and not self.stop.has_key(word):
                        text.append(word)
            i.close()
            yield self.dictionary.doc2bow(text,allow_update=True)

class TopicModel():
    
    def train(self, corpus, num, outputFile="log.txt"):
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO,filename=outputFile)

        tfidf = models.TfidfModel(corpus)
        corpus_tfidf = tfidf[corpus]

        model = models.ldamodel.LdaModel(corpus_tfidf, id2word = corpus.dictionary, num_topics = num)
        model.show_topics(topics=-1, topn=100, log=True)
