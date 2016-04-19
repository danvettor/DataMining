
import numpy as np
import random
import csv

class Delta:
    def __init__(self, eta=0.05, tolerancia=0.1):
        self.tolerancia = tolerancia
        self.eta = eta
        self.w = []
        self.w0 = random.uniform(-10,10)
        

    def leTreino(self):
        X = []
        y = []
        cr = csv.reader(open("dataset.csv","rb"))
        for row in cr:
            row = row[0].split(';')
            for j in range(len(row)):
                row[j] = float(row[j])
            y.append(row.pop())
            X.append(row)
        self.w = [random.uniform(-10,10) for i in xrange(len(row))]
        return (X,y)
        
    def leTeste(self):
        X = []
        cr = csv.reader(open("test.csv","rb"))
        for row in cr:
            row = row[0].split(';')
            for j in range(len(row)):
                row[j] = float(row[j])
            X.append(row)
        return X

    def erro(self, y, yEstimado):
        return np.abs(y - yEstimado)
        

    def fit(self, X, y):
        erroAnterior = 0
        variacaoErro = 1
        while variacaoErro > self.tolerancia:
            erroTotal = 0
            for i in range(len(X)):
                yEstimado = 1 / (1 - np.exp(-np.dot(self.w, X[i])))
                erro = self.erro(y[i], yEstimado)
                erroTotal += erro
                self.w = self.ajustaPlano(self.w, erro, X[i])
                self.w0 = self.w0 * self.eta * erro
            variacaoErro = np.abs(erroAnterior - erroTotal)
            erroAnterior = erroTotal
        print self.w

    def ajustaPlano(self, w, erro, xi):
        w = w + erro * self.eta * xi
        return w

    def predict(self, X):
        if np.dot(self.w,X) >= 0:
            return 1
        else:
            return 2

delta = Delta()
Xtreino, y = delta.leTreino()
delta.fit(Xtreino, y)
Xteste = delta.leTeste()
for i in range(len(Xteste)):
    print(delta.predict(Xteste[i]))
