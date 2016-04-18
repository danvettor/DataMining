
import numpy as np
import random
import csv

class Delta:
    def __init__(self, eta=0.05, tolerancia=0.1):
        self.tolerancia = tolerancia
        self.eta = eta
        self.w = []
        self.w0 = random.uniform(-10,10)
        self.y = []

    def leTreino(self):
        self.X = []
        cr = csv.reader(open("dataset.csv","rb"))
        for row in cr:
            row = row[0].split(';')
            for j in range(len(row)):
                row[j] = float(row[j])
            self.y.append(row.pop())
            self.X.append(row)
        self.w = [random.uniform(-10,10) for i in xrange(len(row))]
        
    def leTeste(self):
        self.X = []
        cr = csv.reader(open("test.csv","rb"))
        for row in cr:
            row = row[0].split(';')
            for j in range(len(row)):
                row[j] = float(row[j])
            self.X.append(row)

    def fit(self):
        erroAnterior = 0
        variacaoErro = 1
        while variacaoErro > self.tolerancia:
            erroTotal = 0
            for i in range(len(self.X)):
                yEstimado = 1 / (1 - np.exp(-np.dot(self.w, self.X[i])))
                erro = np.abs(self.y[i] - yEstimado)
                erroTotal += erro
                self.w = self.ajustaPlano(self.w, erro, self.X[i])
                self.w0 = self.w0 * self.eta * erro
            variacaoErro = np.abs(erroAnterior - erroTotal)
            erroAnterior = erroTotal

    def ajustaPlano(self, w, erro, xi):
        w = w + erro * self.eta * xi
        return w

    def predict(self,X):
        if np.dot(self.w,X) >= self.w[0]:
            return 1
        else:
            return -1

delta = Delta()
delta.leTreino()
delta.fit()
delta.leTeste()
delta.predict()