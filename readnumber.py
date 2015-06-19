from numpy import *
import os
from knn import *

def img2vector(filename):
    f=file(filename)
    f=f.readlines()
    imgvector=[]
    for i in xrange(len(f)):
        for j in xrange(len(f[i].strip())):
            imgvector.append(int(f[i][j]))
    return array(imgvector)

def loadDataSet():
    datasetFiles=os.listdir('trainingDigits')
    numSamples = len(datasetFiles)
    labels=[]
    group=[]
    for i in xrange(numSamples):
        filename = datasetFiles[i]
        labels.append(filename[0])
        vec=img2vector('trainingDigits/'+filename)
        group.append(vec)
    dataset = createDataset(array(group),labels)
    return dataset

def testCorrectRate(dataset,k):
    datasetFiles=os.listdir('testDigits')
    numSamples = len(datasetFiles)
    correct=0
    result=[]
    for i in xrange(numSamples):
        #print "%d/%d" %((i+1),numSamples)
        filename = datasetFiles[i]
        testdata = img2vector('testDigits/'+filename)
        re=knnclassify(testdata,dataset,k)
        if (re==filename[0]):
            correct=correct+1
        result.append([re,filename[0]])
    rate = " %d / %d" %(correct,numSamples)
    print rate
    return result
