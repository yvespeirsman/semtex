

class LanguageGuesser:

    def  __init__(self):
        self.frenchStop = {}
        self.germanStop = {}
        self.dutchStop = {}

        with open('french-stop-words.txt','r') as f:
            for line in f:
                self.frenchStop[line.strip()] = 1
        with open('german-stop-words.txt','r') as f:
            for line in f:
                self.germanStop[line.strip()] = 1
        with open('dutch-stop-words.txt','r') as f:
            for line in f:
                self.dutchStop[line.strip()] = 1

    def guessLanguage(self, listOfWords):
        d = 0
        f = 0
        g = 0
        for word in listOfWords:
            if self.frenchStop.has_key(word):
                f += 1
            if self.dutchStop.has_key(word):
                d += 1
            if self.germanStop.has_key(word):
                g += 1

        if d > f and d > g:
            return "dutch"
        elif f > d and f > g:
            return "french"
        else:
            return "german"

