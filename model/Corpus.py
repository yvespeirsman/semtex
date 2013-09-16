
class Corpus():
    
    def __init__(self,f):
        self.file = f

    def read(self, filt, length):
        self.texts = []
        i = open(self.file)
        for line in i:
            doc = []
            line = line.strip().split()
            for word in line:
                if not word in filt and len(word) > length:
                    doc.append(word)
            self.texts.append(doc)
        i.close()
 
    def computeFrequencies(self):
        print "computing frequencies"
        self.freqs = {}
        i = open(self.file)
        for line in i:
            line = line.strip().split()
            for word in line:
                if self.freqs.has_key(word):
                    self.freqs[word] += 1
                else:
                    self.freqs[word] = 1
        i.close()
