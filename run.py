import glob
import HTMLDocument
import FrogText
import LanguageGuesser
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
        print fn, lang
        d = {"lemmas": t.lemmas,
             "text": t.tokens,
             "language": lang}

        fo = "articles/json/" + fn + ".json"
        with open(fo,'w') as outFile:
            json.dump(d,outFile)
        
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

addToElastic()
        
 
