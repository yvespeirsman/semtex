

class FrogText:

    def __init__(self,fileName):
        self.lemmas = []
        with open(fileName) as i:
            for line in i:
                if len(line) > 2:
                    self.lemmas.append(line.split("\t")[2])
 
