#!/usr/bin/env python

import numpy as np
import random

class Delta:
	def __init__(self, eta=0.05, tolerancia=0.1):
		self.tolerancia = tolerancia
		self.eta = eta
		self.w = []

	def run(self, X):
		for i in range(len(X)):
			self.w[i] = random.randrange(-10,10)
		erroAnterior = 0
		variacaoErro = 1
		while variacaoErro > self.tolerancia:
			erroTotal = 0
			for i in range(len(X)):
				yEstimado = 1 / (1 - np.exp(np.dot(self.w, X[i])))
				erro = np.abs(y[i] - yEstimado)
				erroTotal += erro
				self.w = ajustaPlano(self.w, erro, X[i])
				self.w0 = self.w0 * self.eta * erro
			variacaoErro = np.abs(erroAnterior - erroTotal)
			erroAnterior = erroTotal

	def ajustaPlano(self, w, erro, xi):
		w = w + erro * self.eta * xi
		return w