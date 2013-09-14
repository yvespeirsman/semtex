import xml.etree.ElementTree as ET
import codecs
import re

class WikiCorpus():
    def __init__(self, f):
        self.file = f

    def read(self):
        
        text = ""
        i = open(self.file)
        for line in i:
            line = re.sub('^<.+?>', '<SPLIT>', line)
            line = re.sub('\n',' ',line)
            if re.search('\w',line):
                text += line
        texts = text.split("<SPLIT>")
        print(texts[:20])

        """
        text = "<data>"
        t = 0
        #i = codecs.open(self.file, encoding="utf-8")
        i = open(self.file, encoding="utf-8")
        for line in i:
            t += 1
            print(t)
            text += line
        i.close()
        text += "</data>"
        
        root = ET.fromstring(text)
        #tree = ET.parse(self.file)
        """
