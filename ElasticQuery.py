import pyes

class ElasticQuery:

    def __init__(self):
        self.conn = pyes.ES(['127.0.0.1:9200'])
        
    def submit(self, term):
        q = pyes.TermQuery("text",term)
        results = self.conn.search(query=q)
        return results
