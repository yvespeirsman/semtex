class StopList(dict):

    def __init__(self,f):
        with open(f) as i:
            for line in i:
                self[line.strip()] = 1


