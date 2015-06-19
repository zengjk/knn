from numpy import *
import os

class data:
    def __init__(self,vec,label):
        self.vec=vec
        self.label=label

group = array([[1.,.9],[1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
labels = ['A','A','B','B']

def createDataset(group,labels):
    dataset=[]
    for i in xrange(len(array(group))):
        dataset.append(data(group[i],labels[i]))
    return dataset

def knnclassify(newinput, dataset, k):
    dis=array([])
    for i in xrange(len(dataset)):
        d = sqrt((newinput-dataset[i].vec).dot(newinput-dataset[i].vec))
        dis=append(dis,d)
    sortedDistIndices = dis.argsort()
    labelsCount = {}
    for i in xrange(k):
        labelk=dataset[sortedDistIndices[i]].label
        labelsCount[labelk]=labelsCount.get(labelk,0)+1
    maxcount=0
    for key,value in labelsCount.items():
        if value > maxcount:
            maxcount = value
            maxindex = key
    return maxindex
