import Matrix

class FrogText:

    def __init__(self,fileName):
        self.lemmas = []
        self.tokens = []
        with open(fileName) as i:
            for line in i:
                line = line.split("\t")
                if len(line) > 2:
                    self.lemmas.append(line[2])
                    self.tokens.append(line[1])


    def getBigrams(self):
        bigrams = Matrix.Matrix()
        for i in range(0, len(self.tokens)-1):
            w1 = self.tokens[i]
            w2 = self.tokens[i+1]
            bigrams.add(w1,w2,1)
        return bigrams
