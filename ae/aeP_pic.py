import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *
from PIL import Image

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
    size = 64
    Di = size**2
    Dh = 4000
    lr = 0.1
    ItrNum = 400
    
    print "Di",Di,"Dh",Dh
    ###
    #   initialize

    pilImg = Image.open("./img/kuroneko64.png")    
    imgArr = np.asarray(pilImg)
    size = int(imgArr[:,0,0].shape[0])
 
    imgArrR = np.zeros_like(imgArr)

    for c in range(3): 
        #input = rand(Di)
        input = np.array([])#imgArr[:,:,c]
        for j in range(size):
            input = np.append(input,imgArr[j,:,c])
        input = input/255            
        Di = input.shape[0]
            
        We = np.array([randn(Dh,Di)])
        We = np.append(We,np.array([randn(Dh,Di)]),axis=0)
        Be = randn(Dh)

        Wd = np.array([randn(Di,Dh)])
        Wd = np.append(Wd,np.array([randn(Di,Dh)]),axis=0)
        Bd = randn(Di)
        
        for i in range(ItrNum):
            
            ###
            #   calc error
            u = We[0].dot(input)
            z = f(u+Be)

            r = f(Wd[0].dot(z)+Bd)
            E = sum((input -r)**2)
            #print "EEEE",input-r

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
        for i in range(size):
            for j in range(size):
                imgArrR[j,i,c] = int(r[i*size+j]*255)
                imgArrR[j,i,3] = 255
                #print r[j*size+i],int(r[j*size+i]*255)
        Er= sum(sum(imgArr -imgArrR))
        print "input",input,"r",r
        print "imgArr",sum(sum(imgArr)),"imgArrR",sum(sum(imgArrR))

    plt.xlim(0)            
    plt.ylim(0)
    plt.savefig("./result/error_size"+str(size)+"_Dh"+str(Dh)+".png")    
    plt.show()
    Image.fromarray(imgArrR).save("./result/rePic_size"+str(size)+"_Dh"+str(Dh)+".png")
"""
    for i in range(Di):

        plt.scatter(i,r1[i],c = "g")
        plt.scatter(i,input[i],c = "b")
        plt.scatter(i,r[i],c = "r")
        
 
    plt.ylim(0,1)
    plt.show()
"""
