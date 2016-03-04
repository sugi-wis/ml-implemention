import cv2
import numpy as np
from numpy.random import *
from PIL import Image
import matplotlib.pyplot as plt
import time
import math

"""
imgMat = Image.open('kuroneko400.png')
imgCv = cv2.imread("kuroneko400.png")

cv2.imshow("pic",imgCv)

imgMat.show()
imgMat.rotate(45).save("hoge.png")


cv2.waitKey(0)
"""
def SetPoints():
#calc dtc and set mean data to points	
	for p in points:
		tmp = [] #dtcs to means from one point
		for m in means:
			sqr = ((p[0]-m)**2)[0]
			tmp.append(sqr[0]+sqr[1])
		p[1] = np.argmin(tmp)

def PlotData():
	
	#plot data
	for p in points:
		col ='black'	
		pos = p[0]
		"""
		if p[1] == 0: col = 'r'
		elif p[1] == 1: col = 'b'
		
		"""
		m = means[p[1]][0]
		#display linear
		plt.plot([pos[0],m[0]],[pos[1],m[1]],color=col)
		#show dot
		plt.scatter(pos[0],pos[1])
		
	for m in means:
		plt.plot(m[0][0],m[0][1], color="k", marker="*", markersize=14)

	plt.pause(0.1)
	#plt.show()
	plt.savefig("plot.png")
	plt.gcf().clear()
	
def ResetMeans():
	#reset mean pos
	tmp = [0 for k in range(K)]
	for k in range(K): means[k] = [0,0]
	
	for p in points:
		means[p[1]] += p[0]
		tmp[p[1]] +=1 
	
	for k in range(K):
		means[k] /= tmp[k]

if __name__ == '__main__':
	startTime = time.time()
	 
	K = 6
	pointNum = 100
	ItrNum = 10

	means = np.array([[rand(2)*100]for i in range(K)])
	#points = np.array([rand(pointNum,2)*100])
	points = np.array([[[random()*100,random()*100],0]for i in range(pointNum)]) #p[0] = pos,p[1]=mData

	for itr in range(ItrNum):
		SetPoints()
		PlotData()
		ResetMeans()	

	print("process time "+str(time.time() - startTime))


	
