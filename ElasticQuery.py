import pyes

class ElasticQuery:

    def __init__(self):
        self.conn = pyes.ES(['127.0.0.1:9200'])
        
    def submit(self, field, term):
        q = pyes.TermQuery(field,term)
        results = self.conn.search(query=q)
        return results
