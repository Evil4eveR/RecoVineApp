import cv2
import imutils
import numpy as np
import math
import collections

from keras.saving.legacy.save import load_model
from scipy.interpolate import interp1d
import os



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def rollVector(vec):
    maior = vec[0]
    value = 0
    i = 0
    for v in vec:
        if v > maior:
            maior = v
            value = i
        i += 1
    return np.roll(vec, -value)


''''
Input: path to the image.
In case you prefer to send the image, just erase the first line.

Output: a number series size 200.
Which is the input for the model.
'''
def createSeries(path):
    mat = cv2.imread(path)

    mRows, mCols, mType = mat.shape
    if mRows>mCols:
        mat = imutils.resize(mat, width=300)
    else:
        mat = imutils.resize(mat, height=300)
    
    mRows, mCols, mType = mat.shape
    
    hsv = cv2.cvtColor(mat, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)

    diff = s.copy()
    diff = cv2.normalize(diff, None, 0, 255, cv2.NORM_MINMAX)
    ret,th = cv2.threshold(s,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    crop = cv2.bitwise_and(mat, mat, mask=th)
    
    contours = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    sCont = np.zeros((mRows,mCols,1), np.uint8)

    cnts = imutils.grab_contours(contours)

    c = max(cnts, key=cv2.contourArea)
    cv2.drawContours(sCont, [c], -1, (255, 0, 0), 2)

    r,g,b = cv2.split(crop)
    
    diff = b.copy()
    diff = cv2.normalize(diff, None, 0, 255, cv2.NORM_MINMAX)
    
    ret,th2 = cv2.threshold(diff,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    crop2 = cv2.bitwise_and(mat, mat, mask=th2)

    contours = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros((mRows,mCols,1), np.uint8)
    contour = np.zeros((mRows,mCols,1), np.uint8)

    cnts = imutils.grab_contours(contours)

    c = max(cnts, key=cv2.contourArea)        
    cv2.drawContours(mask, [c], -1, (255, 0, 0), -1)
    cv2.drawContours(contour, [c], -1, (255, 0, 0), 2)

    mask = cv2.bitwise_and(mask, mask, mask=th2)
    crop3 = cv2.bitwise_and(mat, mat, mask=mask)
    
    r,g,b = cv2.split(crop3)
    median = cv2.medianBlur(b,5)
    medianB = cv2.cvtColor(median, cv2.COLOR_GRAY2RGB)
    
    pointB = cv2.normalize(medianB, None, 0, 255, cv2.NORM_MINMAX)

    for i in range(mRows):
        for j in range(mCols):   
            if pointB[i,j,0]==255:
                x, y = i, j
    
    graph = []

    for v in c:
        for p in v:
            d = int(math.sqrt(math.pow(p[0]-x,2)+math.pow(p[1]-y,2)))
            graph.append(d)
    
    rolled = rollVector(graph)
    norm = rolled / np.amax(rolled)
    xold = range(len(norm))
    f2 = interp1d(xold, norm, kind='cubic')
    xnew = np.linspace(0, len(xold)-1, num=200, endpoint=True)
    sized = f2(xnew)

    return sized


def getmaxid(list):

    a = list.index(max(list))
    list.pop(a)
    b = list.index(max(list))
    if b >= a:
        b += 1
    return [a, b]

def getmaxid2(list):

    a = list.key(max(list.value))
    list.pop(a)
    b = list.key(max(list.value))
    if b >= a:
        b += 1
    return [a, b]

def getResult(List):
    frequency = collections.Counter(List)
    frequency= dict(frequency)
    frequency = {k: v for k, v in sorted(frequency.items(), key=lambda item: item[1])}
    first_value = list(frequency.keys())[0]
    second_value= list(frequency.keys())[1]
    return [first_value,second_value]



def finalresult( Image01 ,Image02):
    fila = []
    s = createSeries(Image01)
    s1 = createSeries(Image02)
    #number of images
    #loop to give pass images memory
    fila.append(s)
    fila.append(s1)
    #fila.append(s2)

    fila = np.array(fila)
    fila = fila.reshape((fila.shape[0], fila.shape[1], 1))
    r = model.predict(fila)
    print(r)

    my_list = list()
    for i in r:
        my_list = my_list + getmaxid(list(i))

    result=getResult(my_list)
    return result

#counter = screen001.countImage()

model = load_model(os.path.dirname(__file__) +'/Model.h5')





#s2 = createSeries("test2.png")





