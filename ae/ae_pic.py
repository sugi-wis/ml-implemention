import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *
from PIL import Image
import time

def f(x):
    return 1./(1+np.e**(np.float128(-x)))

def fd(x):
    return np.e**(-x)/(1+np.e**(-x))**2

if __name__ == '__main__':
    #We[layer][in,out]
    #initialize
    #error 
    #weight
    startTime = time.time()

    L = 1
    Dh = 200
    lr = 0.1
    N = 6000
    CNum = 3
    
###
#   initialize

    pilImg = Image.open("./img/kuroneko16.png").convert("RGB")   
    print pilImg

    imgArr = np.asarray(pilImg)
    imgArrR = np.zeros_like(imgArr)
    #print "img",imgArr.shape,"imgR",imgArrR.shape
    eArr = np.zeros(N)
    Di = imgArr.size/CNum
    logFile = open("log",'a')
    print "Di",Di,"Dh",Dh

    for c in range(CNum): 
    
        input = imgArr[:,:,c].reshape(Di)
        
        input = input/255.            
            
        We = np.array([randn(Dh,Di)])
        We = np.append(We,np.array([randn(Dh,Di)]),axis=0)
        Be = randn(Dh)

        Wd = np.array([randn(Di,Dh)])
        Wd = np.append(Wd,np.array([randn(Di,Dh)]),axis=0)
        Bd = randn(Di)
        
        # i... i th learning
        for n in range(N):         
###
#   calc error
            u = We[0].dot(input)
            z = f(u+Be)

            r = f(Wd[0].dot(z)+Bd)
            eArr[n] = np.sum((input -r)**2)
            
            #print "EEEE",input-r
###
#   revise w,b
            ga = (r**2-1)*(input-r)#4*1

            Wd[0] -= (lr*np.array([z]).T.dot(np.array([ga]))/len(input)).T
            #Wd[0] -= lr*sum(z.dot(ga.T))/len(input)
            
            ep = np.array([Wd[0].T.dot(ga)])
            #print (np.array([input]).T.dot(ep)).shape,We[0].shape
            We[0] -= lr*(np.array([input]).T.dot(ep)).T/len(input)
            
            #plt.scatter(i,E)
        
        print "==="
        print "C:",c,"\n---"
        print "E: ",eArr[0],"->",eArr[N-1]
        #print "x: ",input
        #print "r: ",r            

        plt.plot(range(N),eArr[range(N)])    
        imgArrR[:,:,c] = np.uint8(r.reshape(imgArr[:,:,c].shape)*255)

    pTime = time.time() -startTime
    plt.xlim(0)            
    plt.ylim(0)
    plt.grid()
    plt.title("Di"+str(Di)+"Dh"+str(Dh)+"  time:"+str(pTime))
    plt.savefig("./result/error_Di"+str(Di)+"Dh"+str(Dh)+".png")    
    plt.show()
    Image.fromarray(imgArrR).save("./result/rePicC_Di"+str(Di)+"Dh"+str(Dh)+".png")
    print "process time:",pTime
    logFile.writelines("RGB"+"\tN"+str(N)+"\tDi"+str(Di)+"\tDh"+str(Dh)+"\tE"+str(eArr[N-1])+"\ttime"+str(pTime)+"\n")
