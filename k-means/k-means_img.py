import numpy as np
from numpy.random import *
from PIL import Image
import matplotlib.pyplot as plt
import time

def SetPoints():
	#calc dtc and set mean data to points

	for i in range(imgSize[0]):
		for j in range(imgSize[1]):
			dtcs = [sum((points[i,j] - m)**2) for m in means]
			mData[i,j] = np.argmin(dtcs)
		
def PlotData():
	#plot data
	outImg = np.zeros((256,256,3),dtype = int)

	for i in range(imgSize[0]):
		for j in range(imgSize[1]):
			outImg[i,j] = means[mData[i,j]]
	
	Image.fromarray(np.uint8(outImg)).save("out.png")

def ResetMeans():
	#reset mean pos
	#global means
	
	cntArr = [0]*K
	newMeans = np.zeros(means.shape,dtype = int)

	for i in range(imgSize[0]):
		for j in range(imgSize[1]):
			newMeans[mData[i,j]] += points[i,j]
			cntArr[mData[i,j]] += 1
	for k in range(K):
		if cntArr[k] != 0: means[k] = newMeans[k]/cntArr[k]

if __name__ == '__main__':
	startTime = time.time()
	
	pilImg = Image.open('../img/kuroneko256.png')
	imgArr = np.asarray(pilImg)
	imgSize = np.array(imgArr.shape)[0:2]

	K = 8
	ItrNum = 8
	means = np.array([[randint(256)for i in range(3)]for i in range(K)],dtype = int)
	points = np.array(imgArr[:,:,0:3],dtype = int)
	mData = np.zeros([imgSize[0],imgSize[1]],dtype = int)

	print("first means\n"+str(means)+"\n---")
	
	for itr in range(ItrNum):
		startTime = time.time()
		SetPoints()
		PlotData()
		ResetMeans()	
		
		print("iteration = "+str(itr+1)+"/"+str(ItrNum)+"\n"+str(means))
		print time.time() -startTime

