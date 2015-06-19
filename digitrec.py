from knn import *
from numpy import *
from multiprocessing import Pool
import csv
f1=file('train.csv')
f2=file('test.csv')
reader1=csv.reader(f1)
reader2=csv.reader(f2)
dataset=[]
for line in reader1:
    dataset.append(line)
dataset=dataset[1:]

def str2int(a):
    return map(int,a)

dataset=map(str2int,dataset)
dataset=array(dataset)
group=dataset[:,1:]
labels=dataset[:,0]
dataset=createDataset(group,labels)

def kc(testdata):
    a=knnclassify(testdata,dataset,4)
    print a
    return a

testset=[]
for line in reader2:
    testset.append(line)
testset=testset[1:]

testset=map(str2int,testset)
testset=array(testset)

#pool=Pool()
#result=pool.map(kc,testset)
#pool.close()
#pool.join()


