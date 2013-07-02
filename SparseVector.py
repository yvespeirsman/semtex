import math

class SparseVector(dict):
    
    def __init__(self):
        self.position = {}

    def __init__(self, d):
        self.position = d

    def length(self):
        return math.sqrt(sum([x*x for x in self.position.values()]))

    def add(self, dimension):
        if self.position.has_key(dimension):
            self.position[dimension] += 1
        else:
            self.position[dimension] = 1

    def dotProduct(self, other):
        prod = 0
        for key in self.position:
            if other.position.has_key(key):
                prod += self.position[key]*other.position[key]
        return prod

    def cosine(self, other):
        return self.dotProduct(other) / (self.length() * other.length())
