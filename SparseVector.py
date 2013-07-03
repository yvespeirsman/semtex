import math

class SparseVector(dict):
    """
    TODO: two init functions is impossible
    """

    def length(self):
        return math.sqrt(sum([x*x for x in self.values()]))

    def add(self, dimension):
        if self.has_key(dimension):
            self[dimension] += 1
        else:
            self[dimension] = 1

    def dotProduct(self, other):
        prod = 0
        for key in self:
            if other.has_key(key):
                prod += self[key]*other[key]
        return prod

    def cosine(self, other):
        return self.dotProduct(other) / (self.length() * other.length())
