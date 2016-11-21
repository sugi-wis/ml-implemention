import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *

def f(x):
    return 1/(1+np.e**(-x))

def fd(x):
    return np.e**(-x)/(1+np.e**(-x))**2



if __name__ == '__main__':
    #We[layer][in,out]
    #initialize
    #error 
    #weight
    L = 1
    Di = 10
    Dh = 4
    lr = 0.1
    ItrNum = 1000

    ###
    #   initialize

    input = rand(Di)

    We = np.array([randn(Dh,Di)])
    We = np.append(We,np.array([randn(Dh,Di)]),axis=0)
    Be = randn(Dh)

    Wd = np.array([randn(Di,Dh)])
    Wd = np.append(Wd,np.array([randn(Di,Dh)]),axis=0)
    Bd = randn(Di)
    
    r1 = np.zeros([Di])
    print r1
    for i in range(ItrNum):
        
        ###
        #   calc error
        u = We[0].dot(input)
        z = f(u+Be)

        r = f(Wd[0].dot(z)+Bd)
        E = sum((input -r)**2)
        if i == 0: r1 = r


        if i==1:
            print "E start: ",E
        elif i == ItrNum-1:
            print "E end: ",E
            print "x: ",input
            print "r: ",r
        
        ###
        #   revise w,b
        ga = (r**2-1)*(input-r)#4*1

        Wd[0] -= (lr*np.array([z]).T.dot(np.array([ga]))/len(input)).T
        #Wd[0] -= lr*sum(z.dot(ga.T))/len(input)
        
        ep = np.array([Wd[0].T.dot(ga)])
        #print (np.array([input]).T.dot(ep)).shape,We[0].shape
        We[0] -= lr*(np.array([input]).T.dot(ep)).T/len(input)
        
        plt.scatter(i,E)

        #plt.scatter(i,ga,"r")
        #plt.scatter(i,ep,"b")
         
    plt.show()

    for i in range(Di):

        plt.scatter(i,r1[i],c = "g")
        plt.scatter(i,input[i],c = "b")
        plt.scatter(i,r[i],c = "r")
        j = [i,i]
        plt.plot(j,[r1[i],r[i]],"k")
    
    
    plt.ylim(0,1)
    plt.show()
