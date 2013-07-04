import SparseVector 

class VectorSpace(dict):
    
    def add(self, word, dimension, freq=1):
        
        if not self.has_key(word):
            self[word] = SparseVector.SparseVector()

        self[word].add(dimension, freq)
        

    def computeSimilarityMatrix(self):
        allKeys = self.keys()
        simMatrix = {}
        for i in range(0, len(allKeys)):
            word1 = allKeys[i]
            simMatrix[word1] = {}
            for j in range(i+1, len(allKeys)):
                word2 = allKeys[j]
                simMatrix[word1][word2] = self[word1].cosine(self[word2])
        return simMatrix

