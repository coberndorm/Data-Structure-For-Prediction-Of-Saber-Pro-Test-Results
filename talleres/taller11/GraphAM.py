import numpy as np

class graphAM:

    def __init__(self, size):
        self.matriz = np.zeros(size,size)

    def addArc(self, source, destination, weight):
        self.matriz [source][destination] = weight

    def getSuccesor (self, vertex):
        succesor = []
        for i in range(self.matriz.size):
            if (self.matriz[vertex][i] != 0):
                succesor.append(i)
        return succesor

    def getWeight(self, source, destination):
        return self.matriz[source][destination]
