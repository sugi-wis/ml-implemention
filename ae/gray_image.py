from PIL import Image
import numpy as np

imgArr = np.asarray(Image.open('./img/kuroneko64.png').convert('L'))

print imgArr
imgArr  = imgArr/255.

imgArrR = np.int8(0)-np.int8(imgArr*255)
print imgArrR
print np.sum((imgArrR-imgArr)**2)/imgArr.size
Image.fromarray(imgArrR).save("hoge.png")

