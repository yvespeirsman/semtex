
class Matrix(dict):
    
    def add(self, w1, w2, freq=1):
        if self.has_key(w1):
            if self[w1].has_key(w2):
                self[w1][w2] += freq
            else:
                self[w1][w2] = freq
        else:
            self[w1] = {w2: freq}

    def normalizeRows(self):
        for row in self:
            s = float(sum(self[row].values()))
            for col in self[row]:
                self[row][col] /= s

    def sum(self, other):
        """
        This really needs to be optimized. And by the way, there
        are libraries to do this.
        """
        for row in self:
            if other.has_key(row):
                for col in self[row]:
                    if other[row].has_key(col):
                        self[row][col] += other[row][col]
                for col in other[row]:
                    if not self[row].has_key(col):
                        self[row][col] = other[row][col]
        for row in other:
            if not self.has_key(row):
                self[row] = other[row]
