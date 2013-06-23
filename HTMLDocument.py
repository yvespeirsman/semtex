import re
from BeautifulSoup import BeautifulSoup

class HTMLDocument:
    def __init__(self, document):
        self.html = open(document).read()

    def normalize(self):
        html = BeautifulSoup(self.html,convertEntities=BeautifulSoup.HTML_ENTITIES)
        body = html.findAll("body")[0]
        body = body.prettify()
        body = re.sub('\n','',body)
        body = re.sub('<br \/>','\n',body)
        body = re.sub('<.*?>','',body)
        body = " ".join(re.split(r" +",body))
        return body
