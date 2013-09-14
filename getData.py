from model import WikiCorpus
from model import Text

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
        
        o.write(" ".join(myText.stems))
        o.write("\n")
        
o.close()
