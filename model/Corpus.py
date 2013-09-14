
class Corpus():
    
    def __init__(self,f):
        self.file = f
 
    def computeFrequencies():
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
