import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *
from PIL import Image
import time

def f(x):
    return 1/(1+np.e**(-x))

def fd(x):
    return np.e**(-x)/(1+np.e**(-x))**2

if __name__ == '__main__':
    #We[layer][in,out]
    #initialize
    #error 
    #weight
    startTime = time.time()

    L = 1
    Dh = 3000
    lr = 0.1
    N = 400
    
###
#   initialize

    pilImg = Image.open("./img/kuroneko64.png").convert('L') 
    imgArr = np.asarray(pilImg)
    #imgArr = np.random.rand(10)
    Di = imgArr.size
    print "Di",Di,"Dh",Dh

 
    imgArrR = np.zeros_like(imgArr)
    input = imgArr.reshape(Di)
    input = input/255.

        
    We = np.array([randn(Dh,Di)])
    Be = randn(Dh)

    Wd = np.array([randn(Di,Dh)])
    Bd = randn(Di)
    
    # i th/N learning
    for i in range(N):
        
###
#   calc error
        u = We[0].dot(input)
        z = f(u+Be)

        r = f(Wd[0].dot(z)+Bd)
        E = np.sum((input -r)**2)
        #print "EEEE",input-r

        if i==1:
            print "E start: ",E
        elif i == N-1:
            print "E end: ",E
            print "x: ",input
            print "r: ",r
        
###
#   revise w,b
        ga = (r**2-1)*(input-r)#4*1
        Wd[0] -= (lr*np.array([z]).T.dot(np.array([ga]))/len(input)).T
        
        ep = np.array([Wd[0].T.dot(ga)])
        #print (np.array([input]).T.dot(ep)).shape,We[0].shape
        We[0] -= lr*(np.array([input]).T.dot(ep)).T/len(input)
        
        plt.scatter(i,E)
    
    imgArrR = np.uint8(r.reshape(imgArr.shape)*255)

    plt.xlim(0)            
    plt.ylim(0)
    plt.savefig("./result/gray-error_Di"+str(Di)+"Dh"+str(Dh)+".png")    
    plt.show()
    Image.fromarray(imgArrR).save("./result/rePic-gray_Di"+str(Di)+"Dh"+str(Dh)+".png")
    print "process time:",time.time() -startTime
