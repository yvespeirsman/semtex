import glob
import HTMLDocument
import re


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

