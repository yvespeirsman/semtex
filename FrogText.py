

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

