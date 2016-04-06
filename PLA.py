
class PLA:
    w = []
    def _init_(self):
        self.w = [0,3,5]
       
    def sign(self,num):
        if num >= 0: return 1
        else: return 0
        
    def vectorMult(self, a, b):
        result = 0
        size = len(a)
        for i in range(size):
            result = result + a[i]*b[i]
        return result

    def vectorSum(self, a, b):
        for i in range(len(a)):
            a[i] = a[i]+b[i]
        return a

    def scalarMult(self, a, vec):
        for i in range(len(vec)):
            vec[i] = vec[i]*a
        
    def fit(self,X,y):
        cont = 0
        iteration = 0
        for i in range(len(X)):
            X[i].insert(0,1)
        while True:
            cont = 0
            print self.w
            
            for i in range(len(X)):
                if self.sign(self.vectorMult(self.w, X[i])) != self.sign(y[i]):
                    coco = self.vectorSum(self.w, self.scalarMult(y[i],X[i]))
                    #self.w = self.w + y[i]*X[i]
                    cont+=1
                   # print "count: " + str(cont)
            if cont == 0 or iteration == 10000:
                break
            iteration+=1
            


        return self.w
    
    def predict(self,X):
        if self.vectorMult(self.w,X) >= self.w[0]:
            return 1
        else:
            return -1
    
    


xTrain = [[0,0],[2,2],[4,3],[6,2],[8,1]]
yTrain = [1, 1, -1, -1, -1]
test = PLA()
print "sinal de " + str(yTrain[2]) + "eh" + str(test.sign(yTrain[2]))
newW = test.fit(xTrain, yTrain)
print(newW)

#print(test.predict(xTrain[2]))



