import BeautifulSoup as BS
from datetime import *
import urllib2
import re
import time
import glob

def scrape():
    startdate = date(2012,10,01)
    enddate = date(2012,12,31)
    delta = timedelta(days=1)

    d = startdate
    while d < enddate:
        print d.strftime('%Y-%m-%d')
        dateurl= "http://www.ejustice.just.fgov.be/cgi/summary_body.pl?language=nl&pub_date="+ d.strftime('%Y-%m-%d')

        print dateurl
        html = urllib2.urlopen(dateurl)
        soup = BS.BeautifulSoup(html)
        links = soup.findAll(attrs={"name":re.compile('^\d+$')})

        for link in links:
            print link['name']
            fullLinkUrl = "http://www.ejustice.just.fgov.be/cgi/article_body.pl?language=nl&caller=summary&pub_date=" + d.strftime('%Y-%m-%d') + "&numac=" + link['name']
            print '=>', fullLinkUrl

            article = urllib2.urlopen(fullLinkUrl).read()
            articlehtml = BS.BeautifulSoup(article)

            filename = "articles/" + d.strftime('%Y%m%d') +"-"+link['name']+".html"
            print "==>", filename
            o = open(filename,'w')
            o.write(articlehtml.prettify())
            o.close()
            time.sleep(0.5)
            
        print '-->', 'found', len(links), "links"

        d += delta


scrape()

