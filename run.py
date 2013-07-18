import glob
from model import HTMLDocument, FrogText, LanguageGuesser, SparseVector, StopList, VectorSpace, Matrix, TopicModel, 
import re
import json
import requests
import os

def normalize():
    files = glob.glob('articles/html-new/*')
    for f in files:
        fName = f.split('/')[-1]
        oName = re.sub('.html','.txt',fName)
        oName = "articles/txt-new/" + oName
    
        html = HTMLDocument.HTMLDocument(f)
        txt = html.normalize()

        o = open(oName,'w')
        o.write(txt)
        o.close()
        print oName

def makeJSON():
    files = glob.glob('articles/frog/*')
    languageGuesser = LanguageGuesser.LanguageGuesser()

    for f in files:
        d = {}
        t = FrogText.FrogText(f)

        lang = languageGuesser.guessLanguage(t.lemmas)

        fn = f.split("/")[-1].split(".")[0]
        docid = re.sub('-','',fn)
        print fn, lang
        d = {"lemmas": t.lemmas,
             "text": t.tokens,
             "language": lang,
             "docid": docid}

        fo = "articles/json/" + fn + ".json"
        with open(fo,'w') as outFile:
            json.dump(d,outFile)

#makeJSON()
        
def addToElastic():
    r = requests.get('http://localhost:9200')

    files = glob.glob('articles/json/*')
    id = 0
    for f in files:
        id += 1
        with open(f,'r') as i:
            j = json.load(i)
         
            cm = 'curl -XPUT http://localhost:9200/staatsblad/article/' + str(id) + ' -d \'' + json.dumps(j) + '\''
            os.system(cm)

#addToElastic()
 
ministers = {
    "Rupo":1,
    "Crem":1,
    "Reynders":1,
    "Lanotte":1,
    "Croo":1,
    "Milquet":1,
    "Onkelinx":1,
    "Laruelle":1,
    "Geens":1,
    "Labille":1,
    "Turtelboom":1,
    "Chastel":1,
    "Coninck":1
}

#space = VectorSpace.VectorSpace()
#stopList = StopList.StopList("dutch-stop-words.txt")

def runTopicModel():
    files = glob.glob('articles/frog/*')
    stopList = StopList.StopList("dutch-stop-words.txt")
    corpus = TopicModel.MyCorpus(files, stopList)
    model = TopicModel.TopicModel()
    model.train(corpus,100)

runTopicModel()

def getMinisters():
    files = glob.glob('articles/frog/*')

    for f in files:
        text = FrogText.FrogText(f)
        m = None
        for token in text.tokens:
            for minister in ministers:
                if re.search(minister, token,re.IGNORECASE):
                    m = minister
        if not m == None:
            for lemma in text.lemmas:
                space.add(m,lemma)

    for x in space:
        space[x].removeDimensions(stopList)
                
    simList = []
    mat = space.computeSimilarityMatrix()
    for x in mat:
        for y in mat[x]:
            print x,y,mat[x][y]
            simList.append((mat[x][y], x,y))
    simList.sort()
    simList.reverse()

    print simList

#getMinisters()

allBigrams = Matrix.Matrix()
def learn():
    files = glob.glob('articles/frog/*')

    for f in files:
        print f
        text = FrogText.FrogText(f)
        bi = text.getBigrams()
        allBigrams.sum(bi)

#learn()
#print allBigrams
