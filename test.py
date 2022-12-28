import collections
import math
import os

import cv2
import imutils
import numpy as np
from keras.saving.legacy.save import load_model
from scipy.interpolate import interp1d

file_name = os.path.dirname(__file__) +'/Model.h5'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class Calcul_Result() :
    def __init__(self , ListImage):
        self.value = 0
        self.graph = []
        self.model = load_model(file_name)
        self.Path =ListImage

    def rollVector(self ,vec):
        self.value = 0
        self.maior = vec[0]
        i = 0
        for i in vec :
            for v in vec:
                if v > self.maior:
                    self.maior = v
                    self.value = i
                i += 1
            return np.roll(vec, -self.value)



    def getmaxid(self  , list):
        self.a = list.index(max(list))
        list.pop(self.a)
        self.b = list.index(max(list))
        if self.b >= self.a:
            self.b += 1
        return [self.a, self.b]

    def getmaxid2(self, list ):
        self.a = list.key(max(list.value))
        list.pop(self.a)
        self.b = list.key(max(list.value))
        if self.b >= self.a:
            self.b += 1
        return [self.a, self.b]

    def getResult(self , List):
        self.frequency = collections.Counter(List)
        self.frequency = dict(self.frequency)
        self.frequency = {k: v for k, v in sorted(self.frequency.items(), key=lambda item: item[1])}
        self.first_value = list(self.frequency.keys())[0]
        self.second_value = list(self.frequency.keys())[1]
        return [self.first_value, self.second_value]

    def finalresult(self ):
        self.fila = []
        self.rporcent = []

        # number of images
        # loop to give pass images memory
        for i in self.Path :
            self.fila.append(self.createSeries(i))
            print(i)


        # fila.append(s2)

        self.fila = np.array(self.fila)
        self.fila = self.fila.reshape((self.fila.shape[0], self.fila.shape[1], 1))
        self.r = self.model.predict(self.fila)
        print(self.r)


        self.indices = sorted(
        range(len(self.r[0])),
        key=lambda index: self.r[0][index],
        reverse=True)
        self.summ = sum(self.r[0])

        """my_list = list()
        for i in self.r:
            my_list = my_list + self.getmaxid(list(i))

        result = self.getResult(my_list)
        print(result)
        return result"""
        for i in reversed(sorted(self.r[0])):
            self.rporcent.append(self.percentage(i, self.summ))
        # printing the percentage of the matching classes sorted
        print(self.rporcent)
        # printing the IDs of the matching classes sorted
        print(self.indices)

    def result01(self):
        return self.rporcent
    def result02(self):
        return self.indices

    def percentage(self ,parte, whole):


        self.percentage01 =100 *float(parte)/float(whole)
        return str('%.2f'% self.percentage01)










    def createSeries(self ,path):
        self.mat = cv2.imread(path)
        mRows, mCols, mType = self.mat.shape
        if mRows > mCols:
            self.mat = imutils.resize(self.mat, width=300)
        else:
            self.mat = imutils.resize(self.mat, height=300)
        mRows, mCols, mType = self.mat.shape

        self.hsv = cv2.cvtColor(self.mat, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(self.hsv)
        self.diff = s.copy()
        self.diff = cv2.normalize(self.diff, None, 0, 255, cv2.NORM_MINMAX)
        ret, th = cv2.threshold(s, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.crop = cv2.bitwise_and(self.mat, self.mat, mask=th)
        self.contours = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.sCont = np.zeros((mRows, mCols, 1), np.uint8)
        self.cnts = imutils.grab_contours(self.contours)
        self.c = max(self.cnts, key=cv2.contourArea)
        cv2.drawContours(self.sCont, [self.c], -1, (255, 0, 0), 2)

        r, g, b = cv2.split(self.crop)
        self.diff = b.copy()
        self.diff = cv2.normalize(self.diff, None, 0, 255, cv2.NORM_MINMAX)

        ret, th2 = cv2.threshold(self.diff, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.crop2 = cv2.bitwise_and(self.mat, self.mat, mask=th2)

        contours = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.mask = np.zeros((mRows, mCols, 1), np.uint8)
        self.contour = np.zeros((mRows, mCols, 1), np.uint8)

        self.cnts = imutils.grab_contours(contours)
        self.c = max(self.cnts, key=cv2.contourArea)
        cv2.drawContours(self.mask, [self.c], -1, (255, 0, 0), -1)
        cv2.drawContours(self.contour, [self.c], -1, (255, 0, 0), 2)

        self.mask = cv2.bitwise_and(self.mask, self.mask, mask=th2)
        self.crop3 = cv2.bitwise_and(self.mat, self.mat, mask=self.mask)
        r, g, b = cv2.split(self.crop3)
        self.median = cv2.medianBlur(b, 5)
        self.medianB = cv2.cvtColor(self.median, cv2.COLOR_GRAY2RGB)

        self.pointB = cv2.normalize(self.medianB, None, 0, 255, cv2.NORM_MINMAX)
        for i in range(mRows):
            for j in range(mCols):
                if self.pointB[i, j, 0] == 255:
                    self.x, self.y = i, j


        for v in self.c:
            for p in v:
                self.d = int(math.sqrt(math.pow(p[0] - self.x, 2) + math.pow(p[1] - self.y, 2)))
                self.graph.append(self.d)
        self.rolled = self.rollVector(self.graph)
        self.norm = self.rolled / np.amax(self.rolled)
        self.xold = range(len(self.norm))
        self.f2 = interp1d(self.xold, self.norm, kind='cubic')
        self.xnew = np.linspace(0, len(self.xold) - 1, num=200, endpoint=True)
        sized = self.f2(self.xnew)


        return sized

if __name__ =='__main__' :
    pass
