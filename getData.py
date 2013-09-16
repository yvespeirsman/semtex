from model import WikiCorpus, Text, Corpus
from gensim import corpora, models, similarities

import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

"""
print("reading corpus")
corpus = WikiCorpus.WikiCorpus("/home/yves/Downloads/dutch_wiki.xml")
texts = corpus.read()

print("processing texts")
o = open("dutch_wiki_stems.txt","w")
for text in texts:
    if len(text) > 1:
        myText = Text.Text(text,"dutch")
        myText.tokenize()
        myText.stem()
        
        for x in myText.stems:
            o.write(x.encode('utf-8') + " ")
        o.write("\n")
        
o.close()
"""

stop = {}
stopfile = open('model/lists/dutch-stop-words.txt')
for line in stopfile:
    stop[line.strip()] = 1
stopfile.close()



corpus = Corpus.Corpus('dutch_wiki_stems.txt')
corpus.computeFrequencies()

print "reading corpus"
filter = {}
t = 0
for x in corpus.freqs:
    if corpus.freqs[x] < 3:
        t = t+1
        filter[x] = 1
for x in stop:
    filter[x] = 1

corpus.read(filter, 3)

print "getting dictionary"
dictionary = corpora.Dictionary(corpus.texts)
dictionary.save('tmp/wiki_dutch.dict')

print "converting to bag of words"
corpus = [dictionary.doc2bow(text) for text in corpus.texts]
corpora.MmCorpus.serialize('tmp/wiki_dutch.mm',corpus)

print "training lda model"
lda = models.ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=100)
lda.save('tmp/model.lda')


lda = models.ldamodel.LdaModel.load('tmp/model.lda')
lda.print_topics(100, topn=50)
