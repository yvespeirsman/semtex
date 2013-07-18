import math

class SparseVector(dict):
    """
    TODO: two init functions is impossible
    """

    def length(self):
        return math.sqrt(sum([x*x for x in self.values()]))

    def add(self, dimension, freq=1):
        if self.has_key(dimension):
            self[dimension] += freq
        else:
            self[dimension] = freq

    def dotProduct(self, other):
        prod = 0
        for key in self:
            if other.has_key(key):
                prod += self[key]*other[key]
        return prod

    def cosine(self, other):
        return self.dotProduct(other) / (self.length() * other.length())

    def removeDimensions(self,aStopList):
        for word in aStopList:
            self.pop(word, None)

                
