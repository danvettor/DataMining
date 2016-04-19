#!/usr/bin/env python
import numpy as np
import random
import csv
import plot

class Delta:
    def __init__(self, eta = 0.05, tolerancia = 0.1):
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
        self.w = np.array([random.uniform(-10,10) for i in xrange(len(row))])
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

    def error(self, y, yEstimado):
        erro = 0.0
        for i in xrange(len(y)):
            erro += np.abs(y[i] - yEstimado[i]) 
        return erro


    def fit(self, X, y):
        X = np.array(X)
        erroAnterior = 0
        variacaoErro = 1
        while variacaoErro > self.tolerancia:
            erroTotal = 0
            for i in range(len(X)):
                yEstimado = 1 / (1 + np.exp(-np.dot(self.w, X[i]) + self.w0))
                erro = y[i] - yEstimado
                self.w0 = self.w0 * self.eta * erro        
                self.w = self.ajustaPlano(self.w, erro, X[i])
                erroTotal += erro
                # print "erro do exemplo: " + str(i) + "= "+ str(erro)
            # print "erro total: " + str(erroTotal)
            variacaoErro = np.abs(erroAnterior - erroTotal)
            erroAnterior = erroTotal
            # print "variacao: " + str(variacaoErro)

    def ajustaPlano(self, w, erro, xi):
        return w + erro * self.eta * xi
      
    def predict(self, X):
        X = np.array(X)
        if np.dot(self.w,X) >= 0:
            return 0
        else:
            return 1

delta = Delta()
Xtreino, y = delta.leTreino()
Xtreino = np.array(Xtreino)
delta.fit(Xtreino, y)
Xteste = delta.leTeste()
Xteste = np.array(Xteste)
estimado = []
for i in range(len(Xtreino)):
    estimado.append(delta.predict(Xtreino[i]))
print "erro : " + str(delta.error(y,estimado))
plot.plot(delta.w, delta.w0)